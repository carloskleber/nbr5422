function [t, delta] = densArIncendio(rho, h)
%DENSARINCENDIO Densidade do ar corrigida para temperatura de incendio
% rho - pressão atmosférica local em mmhg (padronizar pra hPa)
% h - altura do cabo relativa a vegetacao em m
% Secao 18
r0 = 760; % pressao referencia em mmhg
t0 = 293; % temp referencia em K
s = 0;
for i = 1:h
  s = s + i^(-0.992);
end
t = 976.94./h * s;
delta = rho * t0 ./ (r0 * (273 + t));
end

