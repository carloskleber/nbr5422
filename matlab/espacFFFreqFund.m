function dffff = espacFFFreqFund(Us, Ftmo, kaff, kzff, kgff)
%% ESPACFFFREQFUND espacamento fase-fase em frequencia fundamental
% 9.3.2.1
dffff = 1.64 * (exp(Us* Ftmo / (750 * kaff * kzff * kgff) - 1)).^0.833;

end
