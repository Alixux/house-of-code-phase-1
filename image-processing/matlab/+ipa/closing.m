function out = closing(img, se)
% CLOSING  (30) Morphological closing = dilation followed by erosion.
%   out = ipa.closing(img)
%   out = ipa.closing(img, se)
    if nargin < 2 || isempty(se), se = strel('square', 3); end
    out = imclose(im2uint8(img), se);
end
