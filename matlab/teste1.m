% Teste estudo 1

%% Dados basicos
% Tensao nominal em kV
Us = 345;
rugTerreno = 'B';
% Altitude em m
alt = 100;
% Densidade relativa do ar
dra = 0.9;
% Umidade absoluta g/m3
h = 11;
regiao = 'SE';
obstaculo = 'vegetacaoPerm';
obstaculoH = 'vegetacaoPerm';
hmax = 0;
% flechas (conforme seção 5) - TODO calcular por critério Cigre
ftipn = 10;
ftips = 12;
flimn = 11;
flims = 13;
% altura media do cabo
hmed = 25;
% Diametro do cabo em m
dcond = 2e-2;
% Comprimento do vão em m
L = 450;
% Diametro do tronco cilíndrico em m
dtc = 0.3;
% Comprimento do tronco cilíndrico em m
Ltc = 10;
% Ângulo de incidência do vento em relacao ao cabo (Figura X)
omega = 0.;
% Vento de referência, período de integração 10 min, periodo de retorno XXX, altura 10 m
VrB = 15;
% Razão entre sobretensões de frente lenta: U+/(U+ + U-)
alpha = 0.33;
% Tipo de gap na torre
% TODO definir tipos de torre que intepretaria todos os gaps presentes.
gap = 'condutorBraco';
% Gap inicial
d = 4;

% Temperaturas obtidas a partir da distribuicao estatistica - vide
% testeAmpEstat.m
temp15 = 59.6511;
temp5 = 67.0690;
temp1 = 72.9359;