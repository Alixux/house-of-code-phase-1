function out = median_filter(img, ksize)
% MEDIAN_FILTER  (16) Median filter (robust to salt & pepper noise).
%   out = ipa.median_filter(img, ksize)
    if nargin < 2, ksize = 3; end
    if mod(ksize, 2) == 0, ksize = ksize + 1; end
    out = medfilt2(im2uint8(img), [ksize ksize]);
end
