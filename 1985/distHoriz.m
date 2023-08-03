function d = distHoriz(u)
%% Distâncias horizontais - método convencional (10.2.1)
f = 60.;
d1 = 0.22 + 0.01 .* du;
d2 = 0.37 .* sqrt(f) + 0.0076 .* du;
d = max(d1, d2);
end