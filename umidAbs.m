function h = umidAbs()
  %% Umidade absoluta do ar
  % formula (4)
  h = (6.11 * r * exp(17.6 * t/(243 + t))) / (0.4615 * (273 + t));
end