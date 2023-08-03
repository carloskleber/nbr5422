function d = clearPPPower(us)
%% Clearance - phase to phase, power frequency voltages
% Table E.5
% Us = highest system voltage (kV rms)
kzpf = 0.91;
d = 1.642 .* (exp(us ./ (750 .* ka .* kzpf .* kgpf)) - 1.).^0.83;