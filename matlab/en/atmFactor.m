function ka = atmFactor(u, h)
%% Atmospheric factor - Table E.2
% u - withstand voltage (kV)
% h - altitude (m)
% O calculo é baseado na IEC 61472, mas como é fornecido na EN como tabela,
% será usado de forma discreta

if (u > 1100)
  if (h >= 3000)
    ka = 0.885;
  elseif (h >= 2500)
    ka = 0.915;
  elseif (h >= 2000)
    ka = 0.938;
  elseif (h >= 1500)
    ka = 0.960;
  elseif (h >= 1000)
    ka = 0.978;
  elseif (h >= 500)
    ka = 0.992;
  elseif (h >= 300)
    ka = 0.996;
  elseif (h >= 100)
    ka = 0.999;
  else
    ka = 1.;
  end
elseif (u > 700)
  if (h >= 3000)
    ka = 0.867;
  elseif (h >= 2500)
    ka = 0.996;
  elseif (h >= 2000)
    ka = 0.923;
  elseif (h >= 1500)
    ka = 0.948;
  elseif (h >= 1000)
    ka = 0.970;
  elseif (h >= 500)
    ka = 0.987;
  elseif (h >= 300)
    ka = 0.993;
  elseif (h >= 100)
    ka = 0.998;
  else
    ka = 1.;
  end
elseif (u > 400)
  if (h >= 3000)
    ka = 0.844;
  elseif (h >= 2500)
    ka = 0.875;
  elseif (h >= 2000)
    ka = 0.906;
  elseif (h >= 1500)
    ka = 0.934;
  elseif (h >= 1000)
    ka = 0.959;
  elseif (h >= 500)
    ka = 0.982;
  elseif (h >= 300)
    ka = 0.990;
  elseif (h >= 100)
    ka = 0.997;
  else
    ka = 1.;
  end
elseif (u > 200)
  if (h >= 3000)
    ka = 0.815;
  elseif (h >= 2500)
    ka = 0.849;
  elseif (h >= 2000)
    ka = 0.883;
  elseif (h >= 1500)
    ka = 0.915;
  elseif (h >= 1000)
    ka = 0.946;
  elseif (h >= 500)
    ka = 0.975;
  elseif (h >= 300)
    ka = 0.985;
  elseif (h >= 100)
    ka = 0.995;
  else
    ka = 1.;
  end
else
  if (h >= 3000)
    ka = 0.798;
  elseif (h >= 2500)
    ka = 0.834;
  elseif (h >= 2000)
    ka = 0.870;
  elseif (h >= 1500)
    ka = 0.904;
  elseif (h >= 1000)
    ka = 0.938;
  elseif (h >= 500)
    ka = 0.970;
  elseif (h >= 300)
    ka = 0.982;
  elseif (h >= 100)
    ka = 0.994;
  else
    ka = 1.;
  end
end