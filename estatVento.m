function [mu, sig] = estatVento(beta, eta)
%% ESTATVENTO Calculo dos parametros estatisticos do vento (media e desvio padrao)
% Distribuicao de Weibull:
% beta - parametro de forma
% eta - parametro de escala
mu = eta * gamma(1 + 1/beta);
sig = eta * sqrt(gamma(1+2/beta) - gamma(1+1/beta).^2);

end