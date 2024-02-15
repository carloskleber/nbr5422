function [kg, alt, pbv] = distVert(tipo, hmax)
  %% Distancia vertical de seguranca
  % tipo - tipo do obstaculo
  % hmax - para alguns obstaculos, altura maxima prevista ou altura existente no terreno
  % Tabela 6
  switch tipo
    case {'pedestre'}
      kg = 1.47;
      alt = 3.90;
      pbv = 4.10;
    case {'maqAgricola'}
      kg = 1.18;
      alt = 4.00;
      pbv = 4.20;
    case {'rodovia'}
      kg = 1.18;
      alt = 5.40;
      pbv = 5.60;
    case {'ferroviaNaoEletrificada'}
      kg = 1.18;
      alt = 6.40;
      pbv = 6.60;
    case {'ferroviaEletrificada'}
      kg = 1.30;
      alt = 9.70;
      pbv = 10.0;
    case {'suporteFerrovia'}
      kg = 1.18;
      alt = hmax;
      pbv = 1.70;
    case {'aguasNavegaveis'}
      kg = 1.47;
      alt = hmax;
      pbv = 4.00;
    case {'aguasNaoNavegaveis'}
      kg = 1.47;
      alt = 3.60;
      pbv = 4.00;
    case {'linhaTransmissao'}
      kg = 1.45;
      alt = hmax;
      pbv = 0.70;
    case {'linhaTelecom'}
      kg = 1.45;
      alt = hmax';
      pbv = 0.70;
    case {'vegetacaoPerm'}
      kg = 1.18;
      alt = hmax;
      pbv = 1.80;
    case {'cultAgricPerm'}
      kg = 1.18;
      alt = hmax;
      pbv = 1.80;
    case {'instalacaoTransp'}
      kg = 1.18;
      alt = hmax;
      pbv = 0.70;
    otherwise
      error("Tipo invalido");
  end
end