function vr = tensaoSupIncendio(rho, h)
%TENSAOSUPINCENDIO Tensao maxima suportavel para densidade do ar corrigida
%para incendio
% rho - densidade do ar corrigida
% h - espacamento em cm (padronizar pra m)
vr = 340 * rho * (1 + 0.54 / sqrt(12.5 * rho)) * h/12.5 / (0.25 * (1 + h/12.5 + sqrt((1 + h/12.5)^2 + 8)));
end

