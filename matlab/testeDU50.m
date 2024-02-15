% equacao U50 isolada
% Calculo da distancia - valida para 4 a 10 m
close all
% plotagem do grafico teorico
a = 0.5;
u50 = 1800:10:3400;
% Isolando d
% ref formula antiga: d = 4 + 0.0020387 .* (-2.2361 .* sqrt(2613287 .*(a-0.33).^2 + 12192650 .* (a-0.33) - 4905 .* u50+17422865) + 3475 .* (a-0.33) + 6725);
%d = (6950*a)/981 - (5^(1/2)*(26132870000*a^2 + 102324405800*a - 49050000*u50 + 137615726543)^(1/2))/49050 + 30161/1962;
% Simplificacao
% ref formula antiga: d = 4 + 0.3193 .* (-sqrt(532.78 .*(a-0.33).^2 + 2485.8 .* (a-0.33) - u50 + 3552.1) + 22.189 .* (a-0.33) + 42.941);
d = 7.0846*a - sqrt(54.3115*a^2 + 212.6589*a - 0.1019.*u50 + 286.0043) + 15.3726;
plot(u50,d,':xb')
hold on

% Formula original - ref. EPRI red book 3rd ed (p. 5-25)
d = 4:0.1:25;
u50 = 1708 + 532.*(a-0.33) + 40.4 .* (a-0.33).^2 + 269 .* (d-4) - 9.81 .* (d-4).^2 + 139 .*(a-0.33).*(d-4);
plot(u50,d,'-r')

% Calculo de U50
us = 10:10:800;
fsfl = 2.4;
zfl = 0.06;
kzfl = 1 - 1.3.*zfl;
kafl = 0.95;
kcs = 1.48;
kg = 1.52;
u50 = 1.4 .* kcs .* sqrt(2) .* us .* fsfl ./ (kafl .* kzfl);

% Aplicando conforme a formula proposta
us = 100:50:1500;
d = espacFFFrenteLenta(us, a, kcs, fsfl, kafl, zfl, kg);
figure;
plot(us, d); grid on
