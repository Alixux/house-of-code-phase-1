function c = cumulative_histogram(img)
% CUMULATIVE_HISTOGRAM  (5) Cumulative histogram (discrete CDF).
%   c = ipa.cumulative_histogram(img)
    c = cumsum(ipa.histogram(img));
end
