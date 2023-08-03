function kg = fatorKgFTFrenteLenta(gap)
%% FATORKGFTFRENTELENTA
% Tabela C.1 (baseada na NBR 8186:2021)
  switch gap
    case {'condutorBraco'}
      kg = 1.45; % Entre 1.36 a 1.58
    case {'condutorJanela'}
      kg = 1.25; % Entre 1.22 a 1.32
    case {'condutorPlanoAbaixo'}
      kg = 1.15; % Entre 1.18 a 1.35
    case {'condutorHasteAbaixo'}
      kg = 1.47; % ?
    case {'condutorEstruturaLateral'}
      kg = 1.45; % Entre 1.28 a 1.63
    case {'estruturaHaste'} % e.g. seccionadora aberta
      kg = 1.35; % Entre 1.03 a 1.66
    otherwise
      error("Tipo invalido");
  end 