function out = opening(img, se)
% OPENING  (29) Morphological opening = erosion followed by dilation.
%   out = ipa.opening(img)
%   out = ipa.opening(img, se)
    if nargin < 2 || isempty(se), se = strel('square', 3); end
    out = imopen(im2uint8(img), se);
end
