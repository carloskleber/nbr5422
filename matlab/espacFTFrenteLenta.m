function dftfl = espacFTFrenteLenta(Us, Kcs, Fsfl, kafl, zfl, kg)
%% ESPACFTFRENTELENTA
% 9.3.1
kzfl = 0.922 * (1-1.3*zfl);
dftfl = 2.17 * exp(Kcs*sqrt(2)*Us*Fsfl/(1080 * sqrt(3) * kafl * kzfl * kg) - 1);
end
