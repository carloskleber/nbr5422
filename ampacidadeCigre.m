function iac = ampacidadeCigre(rac, v, ta, tc, rs, eps, alphas)
%% AMPACIDADECIGRE Modelo de ampaciade Cigre WG 22.12, "The thermal behaviour of overhead conductors", Electra 144, 1992.
% Conforme adotado pela REN ANEEL 905 de 2020, Anexo II (revoga REN 191 2005)
% Dados:
% rac = resistência CA de referência (20 graus C)
% v = velocidade do vento em m/s
% ta = temperatura ambiente em graus C
% tc = temperatura de projeto em graus C
% rs = radiação global em W/m²
% eps = coeficiente de emissividade do condutor
% alphas = coeficiente de absorção do condutor
% h = altura média da LT em m
% delta = ângulo de ataque do vento em graus

sigma  = 5.67e-8; % constante de Stefan-Boltzmann

rtcac = rac .* (1 + alphaac .* (tc - 20));
tf = 0.5 .* (tc + ta); % Temperatura de filme (média das temps. do condutor e do ar)
rr  = d ./ (2 .* (D - 2 .* d)); % rugosidade do cabo

if (v == 0) % convecção natural
  npra = 0.715 - 2.5e-4 .* tf;
  gr = D.^3 .* (tc-t) .* g ./((tf+273) .* vf.^2);
  nu = a2 .* (gr .* npra).^m2;
else if (v < 0.5) % convecção mista
else % convecção forçada
  dra = exp(-1.16e-4 .* h);
  vf = 1.32e-5 + 9.5e-8 .* tf; % viscosidade cinemática do ar
  re  = D .* v .* dra ./ vf;
  if (rr < 0.05)
    b2 = 0.178;
    m2 = 0.633;
  else if (rr < 0.718)
    if (re < 2650)
      b2 = 0.641;
      m2 = 0.471;
    else
      b2 = 0.048;
      m2 = 0.800;
    end
  end
  nu = b2 .* re .^ m2;
end

lambdaf = 2.42e-2 + 7.2e-5 .* tf; % Condutividade térmica do ar
pc = pi .* lambdaf .* (tc - ta).* nu;

pr = sigma .* eps .* pi .* D .* ((t+273).^4 - (ta+273).^4);
qs = alphas .* D .* ib;

iac = sqrt((pc + pr - qs) ./ rtcac); % eq.26 da REN indica "Qc" e "Qr"