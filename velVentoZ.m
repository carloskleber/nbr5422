function vz = velVentoZ(v10, z, rug)
  %% Correcao da velocidade do vento pela altura
  % Formula (17) e tabela 2
    switch rug
    case {'A'}
      alpha = 0.110;
    case {'B'}
      alpha = 0.160;
    case {'C'}
      alpha = 0.220;
    case {'D'}
      alpha = 0.280;
    otherwise
      error("Classe de rugosidade invalida");
  end
  vz = v10 * (z/10).^alpha;
end