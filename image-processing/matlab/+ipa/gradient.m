function out = gradient(img)
% GRADIENT  (25) First-derivative gradient magnitude via Sobel.
%   out = ipa.gradient(img)
    f  = double(im2uint8(img));
    gx = imfilter(f, fspecial('sobel')',  'symmetric');
    gy = imfilter(f, fspecial('sobel'),   'symmetric');
    mag = hypot(gx, gy);
    out = uint8(mag * 255 / (max(mag(:)) + eps));
end
