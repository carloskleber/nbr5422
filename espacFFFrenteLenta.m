function d = espacFFFrenteLenta(Us, alpha, Kcs, Fsfl, kafl, zfl, kg)
%% ESPACFTFRENTELENTA
% 9.3.1
kzfl = 0.922 * (1-1.3*zfl);
d = 2.17 * exp(Kcs*sqrt(2)*Us*Fsfl/(1080 * sqrt(3) * kafl * kzfl * kg) - 1);
if (d > 4)
  u50 = 1.4 * Kcs * sqrt(2) * Us * fsfl / (kafl * kzfl);
  d = 4 + 0.3193 .* (-sqrt(532.78 .*(alpha-0.33).^2 + 2485.8 .* (alpha-0.33) ...
    - u50 + 3552.1) + 22.189 .* (alpha-0.33) + 42.941);
end
if (d > 10)
  warning('espacFFFrenteLenta(): distancia calculada fora da validade do modelo: %d m.', d);
end

end
