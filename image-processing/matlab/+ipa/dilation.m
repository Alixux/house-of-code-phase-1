function out = dilation(img, se)
% DILATION  (27) Morphological dilation with structuring element se.
%   out = ipa.dilation(img)              % 3x3 square
%   out = ipa.dilation(img, se)          % supply your own strel
    if nargin < 2 || isempty(se), se = strel('square', 3); end
    out = imdilate(im2uint8(img), se);
end
