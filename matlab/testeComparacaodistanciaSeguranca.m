% testeComparacaodistanciaSeguranca
% Comparacao de distancias de seguranca para diversos obstaculos
Vnom = [69 138 230 345 440 500 765];
obstac = {
'pedestre',
'maqAgricola',
'rodovia',
'ferroviaNaoEletrificada',
'ferroviaEletrificada',
'suporteFerrovia',
'aguasNavegaveis',
'aguasNaoNavegaveis',
'linhaTransmissao',
'linhaTelecom',
'vegetacaoPerm',
'cultAgricPerm',
'instalacaoTransp'};

Dvtipn = zeros(length(Vnom),length(obstac));
Dvtips = zeros(length(Vnom),length(obstac));
Dvlimn = zeros(length(Vnom),length(obstac));
Dvlims = zeros(length(Vnom),length(obstac));

hmax = 0;
Pstip = 0.90;
Pslim = 0.60;
Kcstip = 1.51;
Kcslim = 1.40;
alt = 100;
% Densidade relativa do ar
dra = 0.9;
% Umidade absoluta g/m3
h = 11;
kafl = fatorAtmFrenteLenta(dra, h, d);
for i = 1:length(Vnom),
  for j = 1:length(obstac),
    [kg, alt, Pbv] = distVert(obstac{j}, hmax);
    % Parcelas eletricas por condicao
    Petip = espacFTFrenteLenta(Us, Kcstip, Fsfl, kafl, zfl, kg);
    Pelim = espacFTFrenteLenta(Us, Kcslim, Fsfl, kafl, zfl, kg);
    % 7.2.2.2. Dist vertical, temperatura limite nominal
    Dvlimn(i,j) = Pbv + Pslim + Pelim;
    % 7.2.2.1 Dist vertical, temperatura tipica nominal
    Dvtipn1 = Pbv + Pstip + Petip;
    Dvtipn2 = Dvlimn(i,j) + 0.9;
    Dvtipn(i,j) = max(Dvtipn1, Dvtipn2);
    % 7.2.3.1. Dist vertical, temperatura tipica sobrecorrente
    Dvtips(i,j) = Pbv + Pslim + Petip;
    % 7.2.3.2 Dist vertical, temperatura limite sobrecorrente
    Dvlims(i,j) = Pbv + Pelim;
  end
end

