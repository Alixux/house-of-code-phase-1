function out = min_filter(img, ksize)
% MIN_FILTER  (17a) Non-linear minimum filter.
%   out = ipa.min_filter(img, ksize)
    if nargin < 2, ksize = 3; end
    out = ordfilt2(im2uint8(img), 1, true(ksize));
end
