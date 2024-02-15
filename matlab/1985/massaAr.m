function mu = massaAr(alt, t)
% MASSAAR Massa especifica do ar - versao NBR 5422:1985
mu = 1.293./(1 + 0.00367 .* t) .* (16000 + 64 + t - alt)./(16000 + 64 + t + alt);
end