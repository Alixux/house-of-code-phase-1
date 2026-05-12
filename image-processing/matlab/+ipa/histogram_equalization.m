function out = histogram_equalization(img)
% HISTOGRAM_EQUALIZATION  (9) Classic global histogram equalization.
%   out = ipa.histogram_equalization(img)
    out = histeq(im2uint8(img));
end
