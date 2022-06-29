function d = espacFFFrenteLenta(Us, alpha, Kcs, Fsfl, kafl, zfl, kg)
%% ESPACFTFRENTELENTA
% 9.3.1
kzfl = 0.922 * (1-1.3*zfl);
d = 2.17 * exp(Kcs*sqrt(2)*Us*Fsfl/(1080 * sqrt(3) * kafl * kzfl * kg) - 1);
if (d > 4)
  u50 = 1.4 * Kcs * sqrt(2) * Us * fsfl / (kafl * kzfl);

end
end
