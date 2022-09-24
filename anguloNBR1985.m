function ang = anguloNBR1985(v, q0, d, pcond, Vv, Vp)
%% ANGULONBR1985 Calculo do angulo pelo metodo de 1985
% Sem distincao de angulo na cadeia e meio do vao
K = fatorEfetividadeVento(v);
ang = atan2(K * q0 * d * Vv, pcond * Vp);
end

