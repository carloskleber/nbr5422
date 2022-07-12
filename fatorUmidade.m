function hc = fatorUmidade(h, dra)
%% FATORUMIDADE
% 4.8.3.1
  hc = 1 + 0.0096 .* (h ./ dra - 11);
end

