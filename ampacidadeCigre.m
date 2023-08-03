function iac = ampacidadeCigre(rac, alphaac, v, delta, ta, tc, rs, ep, alphas, h, D, d)
%% AMPACIDADECIGRE Modelo de ampaciade Cigre WG 22.12, "The thermal behaviour of overhead conductors", Electra 144, 1992.
% Conforme adotado pela REN ANEEL 905 de 2020, Anexo II (revoga REN 191 2005)
% Dados:
% rac = resistência CA de referência (20 graus C) em ohm/m
% v = velocidade do vento em m/s
% delta = ângulo de ataque do vento em graus (0 = longitudinal, 90 graus = perpendicular ao conducotr)
% ta = temperatura ambiente em graus C
% tc = temperatura de projeto em graus C
% rs = radiação global em W/m²
% ep = coeficiente de emissividade do condutor
% alphas = coeficiente de absorção do condutor
% alphaac =
% h = altitude média da LT em m
% D = diâmetro do cabo em m
% d = diâmetro dos fios da camada externa em m

sigma  = 5.67e-8; % constante de Stefan-Boltzmann

rtcac = rac .* (1 + alphaac .* (tc - 20));
tf = 0.5 .* (tc + ta); % Temperatura de filme (média das temps. do condutor e do ar)
rr  = d ./ (2 .* (D - 2 .* d)); % rugosidade do cabo
a1 = 0.42;
if (delta < 24)
  b2 = 0.68;
  m1 = 1.08;
else
  b2 = 0.58;
  m1 = 0.90;
end

if (v == 0) % convecção natural
  npra = 0.715 - 2.5e-4 .* tf;
  gr = D.^3 .* (tc-t) .* g ./((tf+273) .* vf.^2);
  nu = a2 .* (gr .* npra).^m2;
elseif (v < 0.5) % convecção mista

else % convecção forçada
  dra = exp(-1.16e-4 .* h);
  vf = 1.32e-5 + 9.5e-8 .* tf; % viscosidade cinemática do ar
  re  = D .* v .* dra ./ vf;
  if (rr < 0.05)
    b2 = 0.178;
    m2 = 0.633;
  elseif (rr < 0.718)
    if (re < 2650)
      b2 = 0.641;
      m2 = 0.471;
    else
      b2 = 0.048;
      m2 = 0.800;
    end
  else

  end
  nu = b2 .* re .^ m2;
  nu = nu .* (a1 + b2 .* (sin(delta)).^ m1);
end

lambdaf = 2.42e-2 + 7.2e-5 .* tf; % Condutividade térmica do ar
pc = pi .* lambdaf .* (tc - ta).* nu;

pr = sigma .* ep .* pi .* D .* ((tc+273).^4 - (ta+273).^4);
qs = alphas .* D .* rs; % Consta "IB" em vez de "RS"
fprintf('rtcac = %g, pc = %f, pr = %f, qs = %f\n', rtcac, pc, pr, qs);

iac = sqrt((pc + pr - qs) ./ rtcac); % eq.26 da REN indica "Qc" e "Qr"

end
