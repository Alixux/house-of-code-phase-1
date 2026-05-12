function out = butterworth_highpass(img, D0, n)
% BUTTERWORTH_HIGHPASS  (22) Butterworth high-pass filter.
%   out = ipa.butterworth_highpass(img, D0, n)
    if nargin < 2, D0 = 30; end
    if nargin < 3, n  = 2;  end
    D = ipa.dist_grid(size(img));
    D(D == 0) = 1e-6;   % avoid /0 at the origin
    H = 1 ./ (1 + (D0 ./ D).^(2 * n));
    out = ipa.frequency_filter(img, H);
end
