function out = gaussian_highpass(img, D0)
% GAUSSIAN_HIGHPASS  (23) Gaussian high-pass filter.
%   out = ipa.gaussian_highpass(img, D0)
    if nargin < 2, D0 = 30; end
    D = ipa.dist_grid(size(img));
    H = 1 - exp(-(D.^2) / (2 * D0^2));
    out = ipa.frequency_filter(img, H);
end
