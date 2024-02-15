function hc = fatorUmidadeCA(h, dra)
%% FATORUMIDADECA
% 4.8.2.2
  hc = 1 + 0.012 .* (h ./ dra - 11);
end

