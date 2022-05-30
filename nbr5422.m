% NBR5422 Aplicacao da metodologia proposta na NBR 5422
%
% Formulas referenciadas conforme numeracao do draft
%
% Carlos Kleber C. Arruda, carloska@cepel.br
function nbr5422

rugTerreno = 'B';
regiao = 'SE';

Ktur = fatTurb(regiao);

end

function d = dra(p, t)
  %% Densidade relativa do ar
  % formula (1)
  t0 = 20;
  p0 = 1013;
  d = p/p0 * (273+t0)/(273+t);
end

function h = umidAbs()
  %% Umidade absoluta do ar
  % formula (4)
  h = (6.11 * r * exp(17.6 * t/(243 + t))) / (0.4615 * (273 + t));
end

function Krug = fatCorrRug(rug)
  %% Fator de correcao de rugosidade
  % Tabela 1
  switch rug
    case {'A'}
      Krug = 1.08;
    case {'B'}
      Krug = 1.;
    case {'C'}
      Krug = 0.85;
    case {'D'}
      Krug = 0.67;
    otherwise
      error("Classe de rugosidade invalida");
  end
end

function Ktur = fatTurb(regiao)
    %% Fator de turbulencia
  % Tabela 3
  switch regiao
    case {'S'}
      Ktur = 1.08;
    case {'SE', 'CO'}
      Ktur = 1.12;
    case {'N', 'NE'}
      Ktur = 1.16;
    otherwise
      error("Regiao invalida");
  end
end

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

function gc = fatorVentoCabo(rug, h)
  %% Fator combinado de vento aplicado a cabos
  % Tabela 8
  if h < 10
    h = 10;
  end
    switch rug
    case {'A'}
      gc = 0.2914*log(h) + 1.0468;
    case {'B'}
      gc = 0.3733*log(h) + 0.9762;
    case {'C'}
      gc = 0.4936*log(h) + 0.9214;
    case {'D'}
      gc = 0.6153*log(h) + 0.8144;
    otherwise
      error("Classe de rugosidade invalida");
  end
end

function gt = fatorVentoSuporte(rug, h)
  %% Fator combinado de vento aplicado a suportes e cadeias
  % Tabela 9
  if h < 10
    h = 10;
  end
    switch rug
    case {'A'}
      gt = -0.0002*h^2 + 0.0232 * h + 1.4661;
    case {'B'}
      gt = -0.0002*h^2 + 0.0274 * h + 1.6820;
    case {'C'}
      gt = -0.0002*h^2 + 0.0298 * h + 2.2744;
    case {'D'}
      gt = -0.0002*h^2 + 0.0384 * h + 2.9284;
    otherwise
      error("Classe de rugosidade invalida");
  end
end


