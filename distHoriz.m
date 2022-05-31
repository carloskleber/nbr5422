function [kg, pbv] = distHoriz(obstaculo)
switch obstaculo
  case {'edificacao'}
    kg = 1.28;
    pbv = 4.00;
  case {'rodovia', 'ferroviaNaoEletrificada', 'ferroviaEletrificada'}
    kg = 1.28;
    pbv = 1.20;
  case {'vegetacaoPerm'}
    kg = 1.28;
    pbv = 2.00;
  otherwise
    error("Tipo invalido");
end
end
