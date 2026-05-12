function out = spatial_mean(img, ksize)
% SPATIAL_MEAN  (13) k x k box / mean filter.
%   out = ipa.spatial_mean(img, ksize)
    if nargin < 2, ksize = 3; end
    k   = fspecial('average', ksize);
    out = ipa.convolve(img, k);
end
