function out = dynamic_threshold(img, blockSize, C)
% DYNAMIC_THRESHOLD  (8) Adaptive thresholding via local mean - C.
%   out = ipa.dynamic_threshold(img, blockSize, C)
    if nargin < 2, blockSize = 31; end
    if nargin < 3, C         = 5;  end
    if mod(blockSize, 2) == 0, blockSize = blockSize + 1; end
    img = im2uint8(img);
    localMean = imfilter(double(img), fspecial('average', blockSize), ...
                         'replicate');
    out = uint8(double(img) >= localMean - C) * 255;
end
