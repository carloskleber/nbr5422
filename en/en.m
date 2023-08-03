 function en(arq)
% EN Aplicação da metodologia da EN 50341-1:2012
%
% Carlos Kleber C. Arruda, carloska@cepel.br
%
% Utiliza os mesmos parâmetros da rotina nbr5422.m, para efeitos de comparação.

run(arq);

% Annex E - air clearances

% gap factors (E.2.5.3)
kgff = 0.74 + 0.26 .* kgsf;
kgpf = 1.35 .* kgsf - 0.35 .* kgsf.^2;

delff = clearPEFastFront(kgff);
dppff = clearPPFastFront(kgff);
delsf = clearPESlowFront(kgsf);
dppsf = clearPPSlowFront(kgsf);
del50 = clearPEPower(kgpf);
dpp50 = clearPPPower(kgpf);

% Annex F - empirical method for mid span clearances

% Ver exemplo do anexo C

