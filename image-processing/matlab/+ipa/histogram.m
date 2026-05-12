function h = histogram(img)
% HISTOGRAM  (4) 256-bin histogram of a grayscale image.
%   h = ipa.histogram(img)
    h = imhist(im2uint8(img));
end
