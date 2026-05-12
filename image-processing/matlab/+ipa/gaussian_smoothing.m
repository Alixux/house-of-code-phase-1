function out = gaussian_smoothing(img, ksize, sigma)
% GAUSSIAN_SMOOTHING  (15) Gaussian low-pass smoothing (spatial domain).
%   out = ipa.gaussian_smoothing(img, ksize, sigma)
    if nargin < 2, ksize = 5;   end
    if nargin < 3, sigma = 1.0; end
    if mod(ksize, 2) == 0, ksize = ksize + 1; end
    k   = fspecial('gaussian', [ksize ksize], sigma);
    out = ipa.convolve(img, k);
end
