function out = laplacian(img)
% LAPLACIAN  (26) Second-derivative Laplacian (absolute value for display).
%   out = ipa.laplacian(img)
    f   = double(im2uint8(img));
    lap = abs(imfilter(f, fspecial('laplacian', 0), 'symmetric'));
    out = uint8(lap * 255 / (max(lap(:)) + eps));
end
