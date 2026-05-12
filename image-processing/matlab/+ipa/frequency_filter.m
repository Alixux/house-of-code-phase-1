function out = frequency_filter(img, H)
% FREQUENCY_FILTER  (14) Apply a centred frequency-domain mask H via FFT/IFFT.
%   out = ipa.frequency_filter(img, H)   % H must match size(img)
    F = fftshift(fft2(double(img)));
    G = F .* H;
    g = real(ifft2(ifftshift(G)));
    out = uint8(min(255, max(0, g)));
end
