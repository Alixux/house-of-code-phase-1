function out = subtract_images(a, b)
% SUBTRACT_IMAGES  (2) Absolute difference of two grayscale images.
%   out = ipa.subtract_images(a, b)
    out = imabsdiff(im2uint8(a), im2uint8(b));
end
