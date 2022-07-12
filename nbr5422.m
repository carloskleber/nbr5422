% NBR5422 Aplicacao da metodologia proposta na NBR 5422
%
% Formulas referenciadas conforme draft de 27/06/2022
%
% Carlos Kleber C. Arruda, carloska@cepel.br
%
% Uso: configura um caso em um script a parte (vide exemplos), chamando no final esta rotina

% 4.8.5 - Fator de correcao atmosferico
kafl = fatorAtmFrenteLenta(dra, h, d);
% 4.10.3.7 - Fator de correcao de rugosidade
Vr = fatCorrRug(rugTerreno) * VrB;
% 4.10.3.9 - Fator de turbulencia;
Vp10 = Vr * fatTurb(regiao);
% 4.10.3.10
Vp3 = Vp * fatTormentas(regiao);
%% 7. Distancias de seguranca
[kg, al, Pbv] = distVert(obstaculo, hmax);
[kg, Pbh] = distHoriz(obstaculoH);
% 7.2.1.2. Parcelas de seguranca
Pstip = 0.90;
Pslim = 0.60;
% 7.2.5. Parcelas eletricas
if ~exist('Kcstip')
  Kcstip = 1.40;
end
if ~exist('Kcslim')
  Kcslim = 1.32;
end

% Projeto de isolamento
zfl = 0.06;
if ~exist('Fsfl')
  if Us <= 69
    Fsfl = 3
  elseif Us <= 440
    Fsfl = 2.5
  elseif Us <= 525
    Fsfl = 2.3
  else
    Fsfl = 2.2
  end
end

% Parcelas eletricas por condicao
Petip = espacFTFrenteLenta(Us, Kcstip, Fsfl, kafl, zfl, kg);
Pelim = espacFTFrenteLenta(Us, Kcslim, Fsfl, kafl, zfl, kg);
% 7.2.2.2. Dist vertical, temperatura limite nominal
Dvlimn = Pbv + Pslim + Pelim;
% 7.2.2.1 Dist vertical, temperatura tipica nominal
Dvtipn1 = Pbv + Pstip + Petip;
Dvtipn2 = Dvlimn + 0.9;
Dvtipn = max(Dvtipn1, Dvtipn2);
% 7.2.3.1. Dist vertical, temperatura tipica sobrecorrente
Dvtips = Pbv + Pslim + Petip;
% 7.2.3.2 Dist vertical, temperatura limite sobrecorrente
Dvlims = Pbv + Pelim;
fprintf('Distancias verticais:\n');
fprintf('- Condicao tipica, regime nominal:       %.3f m\n', Dvtipn);
fprintf('- Condicao tipica, regime sobrecorrente: %.3f m\n', Dvtips);
fprintf('- Condicao limite, regime nominal:       %.3f m\n', Dvlimn);
fprintf('- Condicao limite, regime sobrecorrente: %.3f m\n', Dvlims);

% 7.3.2. distancia horizontal
Dh = Pbh + Petip;

%% Acao do vento
% Temparatura de referencia para pressao de vento
t = 15;
mu = massaAr(alt, t);

% 8.4.2. Pressao dinamica de referencia - 10 min e 3 s
q010 = 0.5 * mu * Vp10^2;
q03 = 0.5 * mu * Vp3^2;
Cxc = arrastoCabos(d);
Gc = fatorVentoCabo(rugTerreno, h);
Gl = fatorVentoVao(L);
% 8.5.2.2. Acao do vento sobre os cabos
Ac = q010 * Cxc * Gc * Gl * d * L * sin(omega)^2;
fprintf('Acao do vento sobre cabo - vento 10 minutos:\n');
fprintf('- Coeficiente de arrasto (Cxc):  %d\n', Cxc);
fprintf('- Fator combinado de vento (Gc): %d\n', Gc);
fprintf('- Fator de efetividade (Gl):     %d\n', Gl);
fprintf('- Pressao dinamica (q0):         %d Pa\n', q010);

% 8.8.3.1. Forca exercida pelo vento, suporte cilindrico
Atc = q010 * cxtc(d, Vp) * Gt * dtc  * Ltc * (sin(theta)).^3;

% Angulo de balanco


%% Faixa de passagem

