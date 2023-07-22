function d = dra(p, t)
  %% Densidade relativa do ar - seção 4.5.1
  t0 = 20;
  p0 = 1013;
  d = p/p0 * (273+t0)/(273+t);
end