function k = correcaoVentoRetorno(v)
  %% Correcao da velocidade de vento obtida para um tempo de retorno especificado
  % n - numero de anos de coleta de dados
  % t - periodo de retorno
  % vm - velocidade media
  % ktn - valor de frequencia
  % alfa - parametro de localizacao da distribuicao de Gumbel
  % beta - parametro de forma da distribuicao de Gumbel
  i = 1:n;
  zi = -log(-log(i./(n+1)));
  c1 = 1/n * sum(zi);
  c2 = 1/sqrt(n) * sum(zi.^2 - zm.^2);
  ct = -log(-log(1+1/t));
  ktn = (c2-ct)/c1;
  alfa = c1/s;
  beta = vm - c2/s;
end

