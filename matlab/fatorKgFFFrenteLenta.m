function kg = fatorKgFFFrenteLenta(gap, alpha)
if (alpha == 0.5)
  switch gap
    case {'anelAnel'}
      kg = 1.8;
    case {'condutorCruzado'}
      kg = 1.65;
    case {'hasteHaste', 'condutorCondutor', 'condutorParalelo'}
      kg = 1.62;
    case {'barramento'}
      kg = 1.50;
    case {'assimetrico'}
      kg = 1.45;
    otherwise
      error("Tipo invalido");
  end
elseif (alpha == 0.33)
  switch gap
    case {'anelAnel'}
      kg = 1.7;
    case {'condutorCruzado'}
      kg = 1.53;
    case {'hasteHaste', 'condutorCondutor', 'condutorParalelo'}
      kg = 1.52;
    case {'barramento'}
      kg = 1.40;
    case {'assimetrico'}
      kg = 1.36;
    otherwise
      error("Tipo invalido");
  end
else
  error("Fator alpha nao previsto");
end
end