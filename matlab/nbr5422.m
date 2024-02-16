function nbr5422(arq)
% NBR5422 Aplicacao da metodologia proposta na NBR 5422
%
% Formulas referenciadas conforme versao em consulta nacional
%
% Carlos Kleber C. Arruda, carloska@cepel.br
%
% Uso: configura um caso em um script a parte (vide exemplos), chamando no final esta rotina
run(arq);

% 4.8.5 - Fator de correção atmosférico
% Deve-se entrar a distancia no ar antes de calcular os gaps?
kafl = fatorAtmFrenteLenta(dra, h, d);
% 4.9.4.2 - Fator de correcao de rugosidade
Vr = fatCorrRug(rugTerreno) * VrB;
% 4.9.4.3 - Fator de integracao
kint = fatorCorrTint10(rugTerreno);
% 8.2.1.1 - Fator de turbulencia;
Vp = Vr * fatTurb(regiao);
% 8.2.2.1 - Velocidade de 30 s de projeto

% 8.2.3.4 - Velocidade de 3 s de projeto
Vp3s = 1.15 * kint .* Vp;
%% 7. Distâncias de segurança
% TODO ver kg para torre
[kg, al, Pbv] = distVert(obstaculo, hmax);
[kg, Pbh] = distHoriz(obstaculoH);
% 7.2.1.2. Parcelas de segurança
Pstip = 0.90;
Pslim = 0.60;
% 7.2.5. Parcelas elétricas
if ~exist('Kcstip')
  Kcstip = 1.51;
end
if ~exist('Kcslim')
  Kcslim = 1.40;
end

% Projeto de isolamento
zfl = 0.06;
if ~exist('Fsfl')
  if Us <= 69
    Fsfl = 3;
  elseif Us <= 440
    Fsfl = 2.5;
  elseif Us <= 525
    Fsfl = 2.3;
  else
    Fsfl = 2.2;
  end
end

% Pode-se definir o fator Kg na torre ou usar o valor típico pelo tipo do gap
if ~exist('kgtorre')
  kgtorre = fatorKgFTFrenteLenta(gap);
end
kgvao = fatorKgFFFrenteLenta('condutorParalelo', alpha);

% Parcelas eletricas por condição
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
fprintf('Distancias verticais de seguranca:\n');
fprintf('- Condicao tipica, regime nominal:       %.3f m\n', Dvtipn);
fprintf('- Condicao tipica, regime sobrecorrente: %.3f m\n', Dvtips);
fprintf('- Condicao limite, regime nominal:       %.3f m\n', Dvlimn);
fprintf('- Condicao limite, regime sobrecorrente: %.3f m\n', Dvlims);

fprintf('Flechas (modelo Cigre):\n');
fprintf('- Regime nominal:       %.3f m\n', flechan);
fprintf('- Regime sobrecorrente: %.3f m\n', flechas);

htipn = Dvtipn + flechan;
htips = Dvtips + flechas;
hlimn = Dvlimn + flechan;
hlims = Dvlims + flechas;

fprintf('Altura do suporte por condicao:\n');
fprintf('- Condicao tipica, regime nominal:       %.3f m\n', htipn);
fprintf('- Condicao tipica, regime sobrecorrente: %.3f m\n', htips);
fprintf('- Condicao limite, regime nominal:       %.3f m\n', hlimn);
fprintf('- Condicao limite, regime sobrecorrente: %.3f m\n', hlims);

% 7.3.2. distância horizontal
Dh = Pbh + Petip;

%% Ação do vento
% Temperatura de referência para pressão de vento
t = 15;
mu = massaAr(alt, t);

% 8.4.2. Pressão dinâmica de referência - 10 min e 3 s
q010 = 0.5 * mu * Vp10^2;
q03 = 0.5 * mu * Vp3^2;
Cxc = arrastoCabos(d);
Gc = fatorVentoCabo(rugTerreno, h);
Gl = fatorVentoVao(L);
% 8.5.2.2. Ação do vento sobre os cabos
Ac = q010 * Cxc * Gc * Gl * d * L * sin(omega)^2;
fprintf('Acao do vento sobre cabo - vento 10 minutos:\n');
fprintf('- Coeficiente de arrasto (Cxc):  %d\n', Cxc);
fprintf('- Fator combinado de vento (Gc): %d\n', Gc);
fprintf('- Fator de efetividade (Gl):     %d\n', Gl);
fprintf('- Pressao dinamica (q0):         %d Pa\n', q010);

% 8.8.3.1. Força exercida pelo vento, suporte cilindrico
Atc = q010 * cxtc(d, Vp) * Gt * dtc  * Ltc * (sin(theta)).^3;

% Ângulo de balanço
ang = anguloNBR1985(v, q0, d, pcond, Vv, Vp);

% Projeção horizontal

%% Faixa de passagem




