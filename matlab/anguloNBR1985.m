function ang = anguloNBR1985(v, q0, d, pcond, Vv, Vp)
%% ANGULONBR1985 Cálculo do ângulo pelo método de 1985
% Sem distinção de ângulo na cadeia e meio do vão
K = fatorEfetividadeVento(v);
ang = atan2(K * q0 * d * Vv, pcond * Vp);
end

