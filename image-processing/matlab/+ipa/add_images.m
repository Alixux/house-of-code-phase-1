function out = add_images(a, b)
% ADD_IMAGES  (1) Saturated addition of two grayscale images.
%   out = ipa.add_images(a, b)
    out = imadd(im2uint8(a), im2uint8(b));
end
