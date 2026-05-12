function out = ideal_highpass(img, D0)
% IDEAL_HIGHPASS  (21) Ideal high-pass filter: 0 inside D0, 1 outside.
%   out = ipa.ideal_highpass(img, D0)
    if nargin < 2, D0 = 30; end
    D = ipa.dist_grid(size(img));
    H = double(D > D0);
    out = ipa.frequency_filter(img, H);
end
