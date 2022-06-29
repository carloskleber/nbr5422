function dftff = espacFTFreqFund(Us, Ftmo, kaff, kzff, kgff)
%% ESPACFTREQFUND espacamento fase-terra em frequencia fundamental
% 9.3.1.1
dftff = 1.64 * (exp(Us* Ftmo / (750 * sqrt(3) * kaff * kzff * kgff) - 1)).^0.833;

end
