%% teste ampacidade estatistica
% realiza a leitura do arquivo veraoDia.csv, que contem a temperatura do
% condutor calculada a cada hora para cada condicao meteorologica
% e curva de carga registrada.
close all
readCapOper;
temp = cell2mat(veraoDia(:,6));
figure;
histogram(temp,'normalization','pdf');
xlabel('Temperatura');
ylabel('f(t)');
grid on
axis([20 85 0 0.05])
figure;
[f,x,flo,fup] = ecdf(temp, 'function','survivor');
stairs(x,f);
hold on;
stairs(x,flo,'r:'); stairs(x,fup,'r:');
xlabel('Temperatura');
% Na verdade o eixo Y seria a funcao sobrevivencia S(t), mas seguindo a
% convencao no draft de F(t)
ylabel('P(t)');
line([0 63.2], [0.1 0.1], 'Color','red');
line([63.2 63.2], [0 0.1], 'Color','red');
grid on
axis([20 85 -0.02 1.05])
t15 = interp1(f,x,.15)
t5 = interp1(f,x,.05)
t1 = interp1(f,x,.01)