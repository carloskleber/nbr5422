function d = clearPPFastFront(u90)
%% Clearance - phase to phase, fast front overvoltage
% Table E.5
kzff = 0.961;
d = 1.2 .* u90 ./ (530 .* ka .* kzff .* kgff);