"""
ipa.py — Image Processing Algorithms reference library (Python).

Thirty classic image-processing algorithms organised in four chapters:

    Chapter 1 — Elementary operations         (1–3)
    Chapter 2 — Histogram operations          (4–11)
    Chapter 3 — Filtering                     (12–24)
    Chapter 4 — Morphology & derivatives      (25–30)

All routines operate on 2-D grayscale images (``numpy.ndarray``). Inputs are
accepted as either ``uint8`` or floating-point in [0, 1]; outputs are returned
as ``uint8`` unless noted otherwise (``float`` for gradient / Laplacian /
spectrum-domain previews). The functions are intentionally small and
self-contained so they can be read side-by-side with the MATLAB versions.
"""

from __future__ import annotations

import numpy as np
import cv2
from scipy import ndimage, signal


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def _to_float(img: np.ndarray) -> np.ndarray:
    """Cast to float32 in [0, 255] range-preserving form."""
    return img.astype(np.float32)


def _to_uint8(img: np.ndarray) -> np.ndarray:
    """Clip and cast back to uint8."""
    return np.clip(img, 0, 255).astype(np.uint8)


# =========================================================================== #
# Chapter 1 — Elementary operations
# =========================================================================== #

def add_images(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """(1) Saturated addition of two same-size grayscale images."""
    return _to_uint8(_to_float(a) + _to_float(b))


def subtract_images(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """(2) Absolute-difference subtraction of two images."""
    return _to_uint8(np.abs(_to_float(a) - _to_float(b)))


def multiply_images(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """(3) Pixel-wise multiplication, normalised so the output stays in [0, 255]."""
    out = _to_float(a) * _to_float(b) / 255.0
    return _to_uint8(out)


# =========================================================================== #
# Chapter 2 — Histogram operations
# =========================================================================== #

def histogram(img: np.ndarray, bins: int = 256) -> np.ndarray:
    """(4) 256-bin histogram of a grayscale image."""
    hist, _ = np.histogram(img.ravel(), bins=bins, range=(0, 256))
    return hist.astype(np.int64)


def cumulative_histogram(img: np.ndarray, bins: int = 256) -> np.ndarray:
    """(5) Cumulative histogram (discrete CDF) of a grayscale image."""
    return np.cumsum(histogram(img, bins))


def rescale_dynamic(img: np.ndarray,
                    new_min: int = 0,
                    new_max: int = 255) -> np.ndarray:
    """(6) Linearly rescale the intensity dynamic to [new_min, new_max]."""
    f = _to_float(img)
    lo, hi = float(f.min()), float(f.max())
    if hi - lo < 1e-12:
        return np.full_like(img, new_min, dtype=np.uint8)
    out = (f - lo) * (new_max - new_min) / (hi - lo) + new_min
    return _to_uint8(out)


def threshold(img: np.ndarray, t: int = 127) -> np.ndarray:
    """(7) Global (fixed) thresholding — returns a binary image in {0, 255}."""
    return ((img >= t).astype(np.uint8)) * 255


def dynamic_threshold(img: np.ndarray,
                      block_size: int = 31,
                      C: int = 5) -> np.ndarray:
    """(8) Adaptive / dynamic thresholding using a local mean neighbourhood."""
    if block_size % 2 == 0:
        block_size += 1
    return cv2.adaptiveThreshold(
        img.astype(np.uint8), 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
        block_size, C,
    )


def histogram_equalization(img: np.ndarray) -> np.ndarray:
    """(9) Classic global histogram equalization."""
    cdf = cumulative_histogram(img)
    cdf_norm = cdf * 255.0 / cdf[-1]
    return cdf_norm[img].astype(np.uint8)


def negative(img: np.ndarray) -> np.ndarray:
    """(10) Photographic negative: I' = 255 - I."""
    return (255 - img.astype(np.int32)).astype(np.uint8)


def exponential_transform(img: np.ndarray,
                          mode: str = "gamma",
                          gamma: float = 0.5,
                          c: float = 1.0) -> np.ndarray:
    """(11) Non-linear point transforms: ``gamma``, ``log`` or ``exp``."""
    f = _to_float(img) / 255.0
    if mode == "gamma":
        out = c * np.power(f, gamma)
    elif mode == "log":
        out = c * np.log1p(f * 255.0) / np.log1p(255.0)
    elif mode == "exp":
        out = c * (np.expm1(f) / np.expm1(1.0))
    else:
        raise ValueError(f"unknown mode {mode!r}")
    return _to_uint8(out * 255.0)


# =========================================================================== #
# Chapter 3 — Filtering
# =========================================================================== #

def convolve(img: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """(12) 2-D convolution with an arbitrary kernel (border = reflect)."""
    out = signal.convolve2d(_to_float(img), kernel.astype(np.float32),
                            mode="same", boundary="symm")
    return _to_uint8(out)


def spatial_mean(img: np.ndarray, ksize: int = 3) -> np.ndarray:
    """(13) Spatial mean (box) filter — averages a ksize×ksize neighbourhood."""
    kernel = np.ones((ksize, ksize), dtype=np.float32) / (ksize * ksize)
    return convolve(img, kernel)


def frequency_filter(img: np.ndarray, H: np.ndarray) -> np.ndarray:
    """(14) Apply a frequency-domain mask H (same size as img) via FFT/IFFT."""
    F = np.fft.fftshift(np.fft.fft2(_to_float(img)))
    G = F * H
    g = np.real(np.fft.ifft2(np.fft.ifftshift(G)))
    return _to_uint8(g)


def gaussian_smoothing(img: np.ndarray,
                       ksize: int = 5,
                       sigma: float = 1.0) -> np.ndarray:
    """(15) Gaussian low-pass smoothing in the spatial domain."""
    if ksize % 2 == 0:
        ksize += 1
    return cv2.GaussianBlur(img, (ksize, ksize), sigma)


def median_filter(img: np.ndarray, ksize: int = 3) -> np.ndarray:
    """(16) Median filter — strong against salt-and-pepper noise."""
    if ksize % 2 == 0:
        ksize += 1
    return cv2.medianBlur(img.astype(np.uint8), ksize)


def min_filter(img: np.ndarray, ksize: int = 3) -> np.ndarray:
    """(17a) Non-linear minimum filter (morphological erosion with a box)."""
    return ndimage.minimum_filter(img, size=ksize).astype(np.uint8)


def max_filter(img: np.ndarray, ksize: int = 3) -> np.ndarray:
    """(17b) Non-linear maximum filter (morphological dilation with a box)."""
    return ndimage.maximum_filter(img, size=ksize).astype(np.uint8)


def nagao_filter(img: np.ndarray) -> np.ndarray:
    """(18) Nagao–Matsuyama 5×5 edge-preserving filter.

    Nine overlapping sub-windows are evaluated for every pixel and the mean
    of the sub-window with the smallest variance is kept. The result is a
    mild smoothing that preserves edges.
    """
    f = _to_float(img)
    h, w = f.shape
    padded = np.pad(f, 2, mode="reflect")

    # Nine sub-window offsets within a 5×5 neighbourhood (row, col) lists.
    #   W1: centre 3×3, W2..W9: eight directional pentomino-like regions.
    windows = [
        [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
        [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 1), (2, 2), (1, 0), (2, 0)],
        [(0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (2, 2), (2, 3), (1, 4), (2, 4)],
        [(2, 0), (3, 0), (4, 0), (2, 1), (3, 1), (2, 2), (3, 2), (4, 1), (4, 2)],
        [(2, 4), (3, 4), (4, 4), (2, 3), (3, 3), (2, 2), (3, 2), (4, 3), (4, 2)],
        [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2), (2, 1), (2, 2), (2, 0), (0, 2)],
        [(0, 3), (0, 4), (1, 3), (1, 4), (1, 2), (2, 3), (2, 2), (2, 4), (0, 2)],
        [(3, 0), (4, 0), (3, 1), (4, 1), (2, 1), (3, 2), (2, 2), (2, 0), (4, 2)],
        [(3, 3), (4, 3), (3, 4), (4, 4), (2, 3), (3, 2), (2, 2), (2, 4), (4, 2)],
    ]

    # Pre-build index arrays so we can vectorise the per-window statistics.
    means = np.empty((len(windows), h, w), dtype=np.float32)
    variances = np.empty_like(means)
    for k, pts in enumerate(windows):
        stacked = np.stack([padded[r:r + h, c:c + w] for r, c in pts], axis=0)
        means[k] = stacked.mean(axis=0)
        variances[k] = stacked.var(axis=0)

    best = np.argmin(variances, axis=0)
    out = np.take_along_axis(means, best[None, ...], axis=0)[0]
    return _to_uint8(out)


# --- Frequency-domain filter masks ---------------------------------------- #

def _dist_grid(shape: tuple[int, int]) -> np.ndarray:
    """Centered frequency-distance grid for a mask of given shape."""
    rows, cols = shape
    cr, cc = rows // 2, cols // 2
    r = np.arange(rows)[:, None] - cr
    c = np.arange(cols)[None, :] - cc
    return np.sqrt(r * r + c * c).astype(np.float32)


def butterworth_lowpass(img: np.ndarray, D0: float = 30,
                        n: int = 2) -> np.ndarray:
    """(19) Butterworth low-pass filter of cutoff D0 and order n."""
    D = _dist_grid(img.shape)
    H = 1.0 / (1.0 + (D / D0) ** (2 * n))
    return frequency_filter(img, H)


def gaussian_lowpass(img: np.ndarray, D0: float = 30) -> np.ndarray:
    """(20) Gaussian low-pass filter of cutoff D0."""
    D = _dist_grid(img.shape)
    H = np.exp(-(D ** 2) / (2.0 * D0 ** 2))
    return frequency_filter(img, H)


def ideal_highpass(img: np.ndarray, D0: float = 30) -> np.ndarray:
    """(21) Ideal high-pass filter — 0 inside radius D0, 1 outside."""
    D = _dist_grid(img.shape)
    H = (D > D0).astype(np.float32)
    return frequency_filter(img, H)


def butterworth_highpass(img: np.ndarray, D0: float = 30,
                         n: int = 2) -> np.ndarray:
    """(22) Butterworth high-pass filter of cutoff D0 and order n."""
    D = _dist_grid(img.shape)
    # Guard against division by zero at the origin.
    with np.errstate(divide="ignore"):
        H = 1.0 / (1.0 + (D0 / np.maximum(D, 1e-6)) ** (2 * n))
    return frequency_filter(img, H)


def gaussian_highpass(img: np.ndarray, D0: float = 30) -> np.ndarray:
    """(23) Gaussian high-pass filter of cutoff D0."""
    D = _dist_grid(img.shape)
    H = 1.0 - np.exp(-(D ** 2) / (2.0 * D0 ** 2))
    return frequency_filter(img, H)


def bandpass(img: np.ndarray, D_low: float = 20,
             D_high: float = 60) -> np.ndarray:
    """(24) Ideal band-pass filter passing frequencies in [D_low, D_high]."""
    D = _dist_grid(img.shape)
    H = ((D >= D_low) & (D <= D_high)).astype(np.float32)
    return frequency_filter(img, H)


# =========================================================================== #
# Chapter 4 — Morphological & derivative operations
# =========================================================================== #

def gradient(img: np.ndarray) -> np.ndarray:
    """(25) First-derivative gradient magnitude via Sobel operators."""
    gx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)
    mag = np.hypot(gx, gy)
    return _to_uint8(mag * 255.0 / (mag.max() + 1e-12))


def laplacian(img: np.ndarray) -> np.ndarray:
    """(26) Second-derivative Laplacian (absolute value for display)."""
    lap = cv2.Laplacian(img, cv2.CV_32F, ksize=3)
    lap = np.abs(lap)
    return _to_uint8(lap * 255.0 / (lap.max() + 1e-12))


def _default_kernel(size: int = 3) -> np.ndarray:
    return cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))


def dilation(img: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    """(27) Morphological dilation with a structuring element."""
    return cv2.dilate(img, kernel if kernel is not None else _default_kernel())


def erosion(img: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    """(28) Morphological erosion with a structuring element."""
    return cv2.erode(img, kernel if kernel is not None else _default_kernel())


def opening(img: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    """(29) Morphological opening — erosion followed by dilation."""
    k = kernel if kernel is not None else _default_kernel()
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, k)


def closing(img: np.ndarray, kernel: np.ndarray | None = None) -> np.ndarray:
    """(30) Morphological closing — dilation followed by erosion."""
    k = kernel if kernel is not None else _default_kernel()
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, k)
