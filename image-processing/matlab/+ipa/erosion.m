function out = erosion(img, se)
% EROSION  (28) Morphological erosion with structuring element se.
%   out = ipa.erosion(img)
%   out = ipa.erosion(img, se)
    if nargin < 2 || isempty(se), se = strel('square', 3); end
    out = imerode(im2uint8(img), se);
end
