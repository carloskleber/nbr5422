function [kg, pbv] = distHoriz(obstaculo)
  %% Distancia horizontal de seguranca
  % tipo - tipo do obstaculo
  % Tabela 7
switch obstaculo
  case {'edificacao'}
    kg = 1.28;
    pbv = 4.00;
  case {'rodovia', 'ferroviaNaoEletrificada', 'ferroviaEletrificada'}
    kg = 1.28;
    pbv = 0.80;
  case {'vegetacaoPerm'}
    kg = 1.28;
    pbv = 2.00;
  otherwise
    error("Tipo invalido");
end
end
