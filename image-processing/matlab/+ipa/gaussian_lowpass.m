function out = gaussian_lowpass(img, D0)
% GAUSSIAN_LOWPASS  (20) Gaussian low-pass filter.
%   out = ipa.gaussian_lowpass(img, D0)
    if nargin < 2, D0 = 30; end
    D = ipa.dist_grid(size(img));
    H = exp(-(D.^2) / (2 * D0^2));
    out = ipa.frequency_filter(img, H);
end
