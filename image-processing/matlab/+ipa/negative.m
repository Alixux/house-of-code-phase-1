function out = negative(img)
% NEGATIVE  (10) Photographic negative:  out = 255 - img.
%   out = ipa.negative(img)
    out = imcomplement(im2uint8(img));
end
