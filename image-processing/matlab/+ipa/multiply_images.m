function out = multiply_images(a, b)
% MULTIPLY_IMAGES  (3) Pixel-wise multiplication normalised to [0,255].
%   out = ipa.multiply_images(a, b)
    A = double(a);  B = double(b);
    out = uint8(min(255, max(0, A .* B / 255)));
end
