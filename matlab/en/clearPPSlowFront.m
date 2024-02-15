function d = clearPPSlowFront(ue2sf)
%% Clearance - phase to phase, slow front overvoltage
% Table E.5
kzsl = 0.922;
d = 2.174 .* (exp((1.4 .* kcs .* ue2sf)./(1080. .* ka .* kzsl .* kgsl)) - 1.);