%% demo_all.m  -- exercises every algorithm in the +ipa package.
%
% Usage:
%   demo_all                      % uses built-in 'cameraman.tif'
%   demo_all('lena.png')          % uses the supplied image

function demo_all(imgPath)
    if nargin < 1 || isempty(imgPath)
        img = imread('cameraman.tif');
    else
        img = imread(imgPath);
        if size(img, 3) == 3, img = rgb2gray(img); end
    end
    img  = im2uint8(img);
    img2 = circshift(img, [0 10]);     % second operand for binary ops

    R = struct();
    R.add       = ipa.add_images(img, img2);
    R.subtract  = ipa.subtract_images(img, img2);
    R.multiply  = ipa.multiply_images(img, img2);
    R.rescale   = ipa.rescale_dynamic(img);
    R.thresh    = ipa.threshold(img, 128);
    R.dynThr    = ipa.dynamic_threshold(img, 31, 5);
    R.eq        = ipa.histogram_equalization(img);
    R.neg       = ipa.negative(img);
    R.gamma     = ipa.exponential_transform(img, 'gamma', 0.5);
    R.conv      = ipa.convolve(img, [0 -1 0; -1 5 -1; 0 -1 0]);   % sharpen
    R.mean      = ipa.spatial_mean(img, 5);
    R.gauss     = ipa.gaussian_smoothing(img, 5, 1);
    R.median    = ipa.median_filter(img, 3);
    R.minF      = ipa.min_filter(img, 3);
    R.maxF      = ipa.max_filter(img, 3);
    R.nagao     = ipa.nagao_filter(img);
    R.bwLP      = ipa.butterworth_lowpass(img, 40, 2);
    R.gaussLP   = ipa.gaussian_lowpass(img, 40);
    R.idealHP   = ipa.ideal_highpass(img, 30);
    R.bwHP      = ipa.butterworth_highpass(img, 30, 2);
    R.gaussHP   = ipa.gaussian_highpass(img, 30);
    R.bandpass  = ipa.bandpass(img, 20, 60);
    R.grad      = ipa.gradient(img);
    R.lap       = ipa.laplacian(img);
    R.dilate    = ipa.dilation(img);
    R.erode     = ipa.erosion(img);
    R.open      = ipa.opening(img);
    R.close     = ipa.closing(img);

    h = ipa.histogram(img);
    c = ipa.cumulative_histogram(img);

    names = fieldnames(R);
    n     = numel(names);
    cols  = 4;  rows = ceil(n / cols);
    figure('Name', 'ipa demo -- operations');
    for i = 1:n
        subplot(rows, cols, i);
        imshow(R.(names{i}));  title(names{i}, 'Interpreter', 'none');
    end

    figure('Name', 'ipa demo -- histograms');
    subplot(1, 2, 1); bar(h); title('histogram');            xlim([0 255]);
    subplot(1, 2, 2); plot(c); title('cumulative histogram'); xlim([0 255]);
end
