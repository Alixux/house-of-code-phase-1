function out = butterworth_lowpass(img, D0, n)
% BUTTERWORTH_LOWPASS  (19) Butterworth low-pass filter.
%   out = ipa.butterworth_lowpass(img, D0, n)
    if nargin < 2, D0 = 30; end
    if nargin < 3, n  = 2;  end
    D = ipa.dist_grid(size(img));
    H = 1 ./ (1 + (D ./ D0).^(2 * n));
    out = ipa.frequency_filter(img, H);
end
