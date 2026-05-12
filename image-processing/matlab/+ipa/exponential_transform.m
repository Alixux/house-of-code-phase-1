function out = exponential_transform(img, mode, gamma, c)
% EXPONENTIAL_TRANSFORM  (11) Non-linear point transforms.
%   out = ipa.exponential_transform(img)                    % gamma = 0.5
%   out = ipa.exponential_transform(img, 'gamma', gamma, c)
%   out = ipa.exponential_transform(img, 'log',   [],    c)
%   out = ipa.exponential_transform(img, 'exp',   [],    c)
    if nargin < 2 || isempty(mode),  mode  = 'gamma'; end
    if nargin < 3 || isempty(gamma), gamma = 0.5;     end
    if nargin < 4 || isempty(c),     c     = 1.0;     end
    f = double(im2uint8(img)) / 255;
    switch lower(mode)
        case 'gamma', g = c .* f.^gamma;
        case 'log',   g = c .* log1p(f * 255) ./ log1p(255);
        case 'exp',   g = c .* (expm1(f) ./ expm1(1));
        otherwise, error('ipa:badMode', 'unknown mode %s', mode);
    end
    out = uint8(min(255, max(0, g * 255)));
end
