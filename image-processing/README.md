# Image Processing Algorithms — Python & MATLAB

Reference implementations of 30 classic image-processing algorithms, grouped
into four chapters, with matching APIs in Python and MATLAB.

## Contents

```
image-processing/
├── python/
│   ├── ipa.py          # All 30 algorithms (Image Processing Algorithms)
│   ├── demo.py         # End-to-end demo on a grayscale test image
│   └── requirements.txt
└── matlab/
    ├── +ipa/           # MATLAB package: one file per algorithm
    └── demo_all.m      # End-to-end demo
```

## Chapters

1. **Elementary operations** — pixel-wise add / subtract / multiply
2. **Histogram operations** — histogram, CDF, rescale, threshold, dynamic
   threshold, equalization, negative, log / gamma / exponential
3. **Filtering** — convolution, spatial mean, frequency, Gaussian smoothing,
   median, min/max, Nagao, Butterworth LP/HP, Gaussian LP/HP, ideal HP,
   band-pass
4. **Morphology & derivatives** — gradient, Laplacian, dilation, erosion,
   opening, closing

## Python quickstart

```bash
cd image-processing/python
pip install -r requirements.txt
python demo.py path/to/lena.png
```

## MATLAB quickstart

```matlab
cd image-processing/matlab
demo_all            % uses built-in 'cameraman.tif' if no image supplied
```

All functions operate on **grayscale** images. Color images are expected to
be converted beforehand (`cv2.cvtColor` / `rgb2gray`).
