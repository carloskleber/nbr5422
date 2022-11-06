function k = fatorEfetividadeVento(v)
  %% Fator de vento para correção do do ângulo de balanço com a velocidade do vento
  % Figura ?
  if v < 10
    k = 1.0;
  else
    k = 3.7047 * exp(-0.162*v) + 0.3;
  end
end
