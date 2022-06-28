% NBR5422 Aplicacao da metodologia proposta na NBR 5422
%
% Formulas referenciadas conforme draft de 27/06/2022
%
% Carlos Kleber C. Arruda, carloska@cepel.br
%
% Uso: configura um caso em um script a parte (vide exemplos), chamando no final esta rotina

% 4.10.3.7 - Fator de correcao de rugosidade
Vr = fatCorrRug(rugTerreno) * VrB
% 4.10.3.9 - Fator de turbulencia;
Vp = Vr * fatTurb(regiao);
% 4.10.3.10
Vp3 = Vp * fatTormentas(regiao);
%% 7. Distancias de seguranca
[kg, al, Pbv] = distVert(obstaculo, hmax);
[kg, Pbh] = distHoriz(obstaculo);
% 7.2.1.2. Parcelas de seguranca
Pstip = 0.90;
Pslim = 0.60;
% 7.2.5. Parcelas eletricas
Kcstip = 1.40;
Kcslim = 1.32;

% Projeto de isolamento

Petipn = espacFTFrenteLenta(Kcs1);
Pelimn = espacFTFrenteLenta(Kcs2);
% 7.2.2.1 Dist vertical, temperatura tipica nominal
Dvtipn1 = Pbv + Pstip + Petipn;
Dvtipn2 = Dvlimn + 0.9;
Dvtipn = max(Dvtipn1, Dvtipn2);
% 7.2.2.2. Dist vertical, temperatura limite nominal
Dvlimn = Pbv + Pelim + Pelim;
% 7.2.3.1. Dist vertical, temperatura tipica sobrecorrente
Dvtips = Pbv + Pelim + Pstips;
% 7.2.3.2 Dist vertical, temperatura limite sobrecorrente
Dvlims = Pbv + Pelim;

% 7.3.2. distancia horizontal
Dh = Pbh + Petipn;

%% Acao do vento
mu = massaAr(alt);

% 8.4.2. Pressao dinamica de referencia - 10 min e 3 s
q010 = 0.5 * mu * Vp10^2;
q03 = 0.5 * mu * Vp3^2;
% 8.5.2.2. Acao do vento sobre os cabos
Ac = q010 * Cxc * Gc * Gl * d * L * sin(omega)^2;

% 8.8.3.1. Forca exercida pelo vento, suporte cilindrico
Atc = q010 * cxtc(d, Vp) * Gt * dtc  * Ltc * (sin(theta)).^3;

% Angulo de balanco - comparacao


%% Faixa de passagem

