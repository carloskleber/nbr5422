% Teste Julian
% Baseado no arquivo "Seção 7 - Distâncias de Segurança_Rev10.xls" de 28/06/2022
clear all;

% distancia entre linhas 500 e 69 kV
Us = 500 + 69;
Fsfl = 1;
Kcs = 1.60;
% Fator de correção de condições atmosféricas - mas depende da distância do gap, assume-se um valor inicial
kafl = 0.95;
zfl = 0.06;
alpha = 0.5;
kg = fatorKgFFFrenteLenta('condutorCondutor', alpha);
d = espacFFFrenteLenta(Us, alpha, Kcs, Fsfl, kafl, zfl, kg)

