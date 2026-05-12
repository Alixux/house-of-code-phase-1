function out = rescale_dynamic(img, newMin, newMax)
% RESCALE_DYNAMIC  (6) Linear dynamic-range rescale to [newMin, newMax].
%   out = ipa.rescale_dynamic(img)                   % [0,255]
%   out = ipa.rescale_dynamic(img, newMin, newMax)
    if nargin < 2, newMin = 0;   end
    if nargin < 3, newMax = 255; end
    f  = double(img);
    lo = min(f(:));  hi = max(f(:));
    if hi - lo < eps
        out = uint8(newMin * ones(size(img)));
        return;
    end
    out = uint8((f - lo) * (newMax - newMin) / (hi - lo) + newMin);
end
