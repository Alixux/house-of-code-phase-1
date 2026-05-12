function D = dist_grid(sz)
% DIST_GRID  Centred frequency-distance grid for a 2-D array of size sz.
%   D = ipa.dist_grid([rows cols])
    rows = sz(1); cols = sz(2);
    cr = floor(rows / 2);  cc = floor(cols / 2);
    [C, R] = meshgrid((0:cols - 1) - cc, (0:rows - 1) - cr);
    D = sqrt(R.^2 + C.^2);
end
