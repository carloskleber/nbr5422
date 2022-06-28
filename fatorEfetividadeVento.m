function k = fatorEfetividadeVento(v)
  %% Fator de vento para correção do do ângulo de balanço com a velocidade do vento
  % Figura ?
  if v < 10
    k = 1.0;
  else
    k = 3.5 * exp(-0.16*v) + 0.3;
  end
end
