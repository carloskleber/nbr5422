function iec(arq)
% IEC Aplicação da metodologia da IEC 60826:2017
%
% Carlos Kleber C. Arruda, carloska@cepel.br
%
% Utiliza os mesmos parâmetros da rotina nbr5422.m, para efeitos de comparação.

run(arq);

% Table 5
[alpha, kr] = roughness(regiao);

% Reference wind speeed - 6.2.4
vr = kr .* vrb;

% Coordenação de isolamento - IEC 60071-2:2018
