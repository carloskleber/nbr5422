function [kg, alt, pbv] = distVert(tipo, hmax)
  %% Distancia vertical de seguranca
  % tipo - tipo do obstaculo
  % hmax - para alguns obstaculos, altura maxima prevista ou altura existente no terreno
  % Tabela 6
  switch tipo
    case {'pedestre'}
      kg = 1.47;
      alt = 3.90;
      pbv = 4.50;
    case {'maqAgricola'}
      kg = 1.18;
      alt = 4.00;
      pbv = 4.60;
    case {'rodovia'}
      kg = 1.18;
      alt = 5.40;
      pbv = 6.00;
    case {'ferroviaNaoEletrificada'}
      kg = 1.18;
      alt = 6.40;
      pbv = 7.00;
    case {'ferroviaEletrificada'}
      kg = 1.30;
      alt = 9.70;
      pbv = 10.3;
    case {'suporteFerrovia'}
      kg = 1.18;
      alt = hmax;
      pbv = 2.10;
    case {'aguasNavegaveis'}
      kg = 1.47;
      alt = hmax;
      pbv = 4.20;
    case {'aguasNaoNavegaveis'}
      kg = 1.47;
      alt = 3.60;
      pbv = 4.20;
    case {'linhaTransmissao'}
      kg = 1.45;
      alt = hmax;
      pbv = 1.00;
    case {'linhaTelecom'}
      kg = 1.45;
      alt = hmax';
      pbv = 1.00;
    case {'vegetacaoPerm'}
      kg = 1.18;
      alt = hmax;
      pbv = 2.00;
    case {'cultAgricPerm'}
      kg = 1.18;
      alt = hmax;
      pbv = 2.00;
    case {'instalacaoTransp'}
      kg = 1.18;
      alt = hmax;
      pbv = 1.00;
    otherwise
      error("Tipo invalido");
  end
end