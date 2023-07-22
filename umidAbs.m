function h = umidAbs(dra, t)
  %% Umidade absoluta do ar (seção 4.6.1)
  % Usando dra (em pu), ao contrário da fórmula que pede em porcentagem.
  % 
  h = (611. * dra * exp(17.6 * t/(243 + t))) / (0.4615 * (273 + t));
end