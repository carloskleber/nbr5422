function d = clearPESlowFront(ue2sf)
%% Clearance - phase to earth, slow front overvoltage
% Table E.5
% ue2sf = 2% slow-front overvoltage phase to earth stressing the air gap
% (i.e. slow-front overvoltage having a probability of 2% of being exceeded)
kzsl = 0.922;
d = 2.174 .* (exp((kcs .* ue2sf)./(1080. .* ka .* kzsl .* kgsl)) - 1.);