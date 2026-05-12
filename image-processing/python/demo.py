"""End-to-end demo that exercises every algorithm in ``ipa``.

Usage:
    python demo.py                       # uses a synthetic test pattern
    python demo.py path/to/lena.png      # uses your own grayscale image
"""

from __future__ import annotations

import sys
import numpy as np
import cv2
import matplotlib.pyplot as plt

import ipa


def load_image(path: str | None) -> np.ndarray:
    if path:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            raise FileNotFoundError(path)
        return img
    # Fallback: synthetic 256x256 gradient + checkerboard.
    y, x = np.mgrid[0:256, 0:256]
    base = ((x + y) // 2).astype(np.uint8)
    checker = (((x // 16 + y // 16) % 2) * 40).astype(np.uint8)
    return cv2.add(base, checker)


def show(title: str, image: np.ndarray) -> None:
    plt.figure(figsize=(4, 4))
    plt.title(title)
    plt.imshow(image, cmap="gray", vmin=0, vmax=255)
    plt.axis("off")


def main(path: str | None = None) -> None:
    img = load_image(path)
    img2 = np.roll(img, 10, axis=1)      # second operand for binary ops

    results = {
        "01 add":              ipa.add_images(img, img2),
        "02 subtract":         ipa.subtract_images(img, img2),
        "03 multiply":         ipa.multiply_images(img, img2),
        "06 rescale":          ipa.rescale_dynamic(img),
        "07 threshold":        ipa.threshold(img, 128),
        "08 dyn threshold":    ipa.dynamic_threshold(img, 31, 5),
        "09 hist eq":          ipa.histogram_equalization(img),
        "10 negative":         ipa.negative(img),
        "11 gamma 0.5":        ipa.exponential_transform(img, "gamma", 0.5),
        "12 convolve sharpen": ipa.convolve(img, np.array([[0, -1, 0],
                                                           [-1, 5, -1],
                                                           [0, -1, 0]])),
        "13 mean 5x5":         ipa.spatial_mean(img, 5),
        "15 gaussian":         ipa.gaussian_smoothing(img, 5, 1.0),
        "16 median":           ipa.median_filter(img, 3),
        "17 min":              ipa.min_filter(img, 3),
        "17 max":              ipa.max_filter(img, 3),
        "18 nagao":            ipa.nagao_filter(img),
        "19 BW LP":            ipa.butterworth_lowpass(img, 40, 2),
        "20 Gauss LP":         ipa.gaussian_lowpass(img, 40),
        "21 Ideal HP":         ipa.ideal_highpass(img, 30),
        "22 BW HP":            ipa.butterworth_highpass(img, 30, 2),
        "23 Gauss HP":         ipa.gaussian_highpass(img, 30),
        "24 Band-pass":        ipa.bandpass(img, 20, 60),
        "25 gradient":         ipa.gradient(img),
        "26 laplacian":        ipa.laplacian(img),
        "27 dilate":           ipa.dilation(img),
        "28 erode":            ipa.erosion(img),
        "29 open":              ipa.opening(img),
        "30 close":             ipa.closing(img),
    }

    # Histograms are 1-D curves — plot them separately.
    hist = ipa.histogram(img)
    cdf = ipa.cumulative_histogram(img)

    print("histogram sum  =", hist.sum(),  "(should equal number of pixels)")
    print("CDF last value =", cdf[-1])

    cols = 4
    rows = int(np.ceil(len(results) / cols))
    plt.figure(figsize=(cols * 3, rows * 3))
    for i, (name, im) in enumerate(results.items(), start=1):
        plt.subplot(rows, cols, i)
        plt.title(name, fontsize=8)
        plt.imshow(im, cmap="gray", vmin=0, vmax=255)
        plt.axis("off")
    plt.tight_layout()

    plt.figure(figsize=(10, 3))
    plt.subplot(1, 2, 1); plt.title("histogram");            plt.plot(hist)
    plt.subplot(1, 2, 2); plt.title("cumulative histogram"); plt.plot(cdf)

    plt.show()


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
