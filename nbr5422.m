% NBR5422 Aplicacao da metodologia proposta na NBR 5422
%
% Formulas referenciadas conforme numeracao do draft
%
% Carlos Kleber C. Arruda, carloska@cepel.br
function nbr5422

%% Dados basicos
rugTerreno = 'B';
% Altitude em m
alt = 100;
regiao = 'SE';
obstaculo = 'vegetacaoPerm';
hmax = 0;
% Diametro do cabo em m
d = 1e-2; 
% Comprimento do vao em m
L = 450;
% Angulo de incidencia do vento em relacao ao cabo (Figura X)
omega = 0.;

Ktur = fatTurb(regiao);
%% Distancias de seguranca
[kg, al, Pbv] = distVert(obstaculo, hmax);
[kg, Pbh] = distHoriz(obstaculo);
% Formula 19 - Dist vertical, temperatura tipica nominal
Dvtipn1 = Pbv + Pstip + Petipn;
% Formula 20
Dvtipn2 = Dvlimn + 0.9;
Dvtipn = max(Dvtipn1, Dvtipn2);
% Formula 19 - Dist vertical, temperatura limite nominal
Dvlimn = Pbv + Pelim + Pelim;
% Formula 19 - Dist vertical, temperatura tipica sobrecorrente
Dvtips = Pbv + Pelim + Pstips;
% Formula 19 - Dist vertical, temperatura limite sobrecorrente
Dvlims = Pbv + Pelim;

Dh = Pbh + Petipn;

%% Acao do vento
% Formula 18 - Velocidade do vento para projeto
Vp = Ktur * Vr;
mu = massaAr(alt);

% Formula XX - Pressao dinamica de referencia
q0 = 0.5 * mu * Vp^2;
% Formula 32 - Acao do vento sobre os cabos
Ac = q0 * Cxc * Gc * Gl * d * L * sin(omega)^2;


%% Faixa de passagem


end
