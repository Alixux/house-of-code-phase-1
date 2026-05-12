function out = convolve(img, kernel)
% CONVOLVE  (12) 2-D convolution with an arbitrary kernel.
%   out = ipa.convolve(img, kernel)
    out = uint8(min(255, max(0, ...
        imfilter(double(img), kernel, 'symmetric', 'conv'))));
end
