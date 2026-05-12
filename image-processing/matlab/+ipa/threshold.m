function out = threshold(img, t)
% THRESHOLD  (7) Global (fixed) thresholding -> binary {0,255}.
%   out = ipa.threshold(img)          % t = 127
%   out = ipa.threshold(img, t)
    if nargin < 2, t = 127; end
    out = uint8(im2uint8(img) >= t) * 255;
end
