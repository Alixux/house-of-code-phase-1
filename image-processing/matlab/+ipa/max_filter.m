function out = max_filter(img, ksize)
% MAX_FILTER  (17b) Non-linear maximum filter.
%   out = ipa.max_filter(img, ksize)
    if nargin < 2, ksize = 3; end
    out = ordfilt2(im2uint8(img), ksize * ksize, true(ksize));
end
