function out = nagao_filter(img)
% NAGAO_FILTER  (18) Nagao-Matsuyama 5x5 edge-preserving filter.
%
%   For each pixel nine overlapping 9-pixel sub-windows of the surrounding
%   5x5 neighbourhood are considered; the mean of the sub-window with the
%   smallest variance is kept.  The result is a mild smoothing that
%   preserves edges well.

    f = double(im2uint8(img));
    P = padarray(f, [2 2], 'symmetric');
    [H, W] = size(f);

    % Nine 9-pixel sub-windows inside the 5x5 neighbourhood
    % (rows / cols are 1-based offsets into P(r:r+H-1, c:c+W-1)).
    W_idx = { ...
        [2 2;2 3;2 4;3 2;3 3;3 4;4 2;4 3;4 4];   % centre 3x3
        [1 1;1 2;1 3;2 2;2 3;3 2;3 3;2 1;3 1];   % NW
        [1 3;1 4;1 5;2 3;2 4;3 3;3 4;2 5;3 5];   % NE
        [3 1;4 1;5 1;3 2;4 2;3 3;4 3;5 2;5 3];   % SW
        [3 5;4 5;5 5;3 4;4 4;3 3;4 3;5 4;5 3];   % SE
        [1 1;1 2;2 1;2 2;2 3;3 2;3 3;3 1;1 3];   % N
        [1 4;1 5;2 4;2 5;2 3;3 4;3 3;3 5;1 3];   % E
        [4 1;5 1;4 2;5 2;3 2;4 3;3 3;3 1;5 3];   % S
        [4 4;5 4;4 5;5 5;3 4;4 3;3 3;3 5;5 3]};  % W

    bestMean = nan(H, W);
    bestVar  = inf(H, W);
    for k = 1:9
        pts = W_idx{k};
        stacked = zeros(9, H, W);
        for p = 1:9
            r = pts(p, 1);  c = pts(p, 2);
            stacked(p, :, :) = P(r:r + H - 1, c:c + W - 1);
        end
        m = squeeze(mean(stacked, 1));
        v = squeeze(var(stacked, 0, 1));
        take = v < bestVar;
        bestMean(take) = m(take);
        bestVar (take) = v(take);
    end
    out = uint8(min(255, max(0, bestMean)));
end
