function out = bandpass(img, Dlow, Dhigh)
% BANDPASS  (24) Ideal band-pass filter passing frequencies in [Dlow, Dhigh].
%   out = ipa.bandpass(img, Dlow, Dhigh)
    if nargin < 2, Dlow  = 20; end
    if nargin < 3, Dhigh = 60; end
    D = ipa.dist_grid(size(img));
    H = double(D >= Dlow & D <= Dhigh);
    out = ipa.frequency_filter(img, H);
end
