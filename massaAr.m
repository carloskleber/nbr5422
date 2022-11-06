function mu = massaAr(alt, t)
% MASSAAR Massa especifica do ar
mu = 1.225 * 288.15/(t + 273.15) * exp(-1.2e-4 * alt);
end

