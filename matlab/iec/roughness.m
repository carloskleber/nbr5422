function [alpha, kr] = roughness(rug)
  switch rug
    case {'A'}
      alpha = 0.10;
      kr = 1.08;
    case {'B'}
      alpha = 0.16;
      kr = 1.;
    case {'C'}
      alpha = 0.22;
      kr = 0.85;
    case {'D'}
      alpha = 0.28;
      kr = 0.67;
    otherwise
      error("Classe de rugosidade invalida");
  end
end