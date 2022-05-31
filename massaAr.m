function mu = massaAr(alt)
% MASSAAR Massa especifica do ar
% Formula 6
mu = 1.225 * 288.15/(t + 273.15) * exp(-1.2e-4 * alt);
end

