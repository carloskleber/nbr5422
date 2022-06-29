% Teste Julian
% Baseado no arquivo "Seção 7 - Distâncias de Segurança_Rev10.xls" de 28/06/2022

% distancia entre linhas 500 e 69 kV
Us = 500 + 69;
Fsfl = 1;
Kcs = 1.60;
kafl = 0.95;
kzfl = 0.922;
alpha = 0.5;
d = espacFFFrenteLenta(Us, alpha, Kcs, Fsfl, kafl, zfl, kg)

