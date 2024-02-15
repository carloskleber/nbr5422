function d = clearPEFastFront(u90)
%% Clearance - phase to earth, fast front overvoltage
% Table E.5
% u90 = Maximum of 90% lightning impulse withstand voltage of the insulator strings
kzff = 0.961;
d = u90 ./ (530 .* ka .* kzff .* kgff);