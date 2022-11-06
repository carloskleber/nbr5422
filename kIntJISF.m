function k = kIntJISF(i, regiao)
  %% fator de tormentas corrigido pelo tempo de integracao - rotina original JISF
  % i - tempo de integracao da media em segundos
  switch regiao
    case {'S'}
      K3s = 1.6;
    case {'SE', 'CO'}
      K3s = 1.8;
    case {'N', 'NE'}
      K3s = 2;
    otherwise
      error("Regiao invalida");
  end
  k = 1 + (K3s - 1) * log(i/600)/log(1/200);
end

