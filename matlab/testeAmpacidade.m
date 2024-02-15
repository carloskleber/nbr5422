%% testeAmpacidade
% Exemplos de validação conforme Cigre WG 22.12
% Exemplo 1 - Condutor Zebra, Iac 600 A, calcula temperatura


% Exemplo 2 - Condutor Zebra, calcula temperatura

% Exemplo 3 - Condutor Zebra, tmax 75 degC, calcula corrente máxima
% clear all

rac = 0.0428e-3; % Ref EPRI Applet CC-4
ncam = 3;
v = 2;
delta = 45;
ta = 40;
tc = 75;
rs = 980;
ep = 0.5;
alphas = 0.5;
alphaac = 0.00403;
h = 1600;
D = 2.86e-2;
d = 3.18e-3;
imax = ampacidadeCigre(rac, alphaac, v, delta, ta, tc, rs, ep, alphas, h, D, d)
