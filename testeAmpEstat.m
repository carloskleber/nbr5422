%% teste ampacidade estatistica
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
ecdf(temp, 'function','survivor');
xlabel('Temperatura');
% Na verdade o eixo Y seria a funcao sobrevivencia S(t), mas seguindo a
% convencao no draft de F(t)
ylabel('F(t)');
line([0 63.2], [0.1 0.1], 'Color','red');
line([63.2 63.2], [0 0.1], 'Color','red');
grid on
axis([20 85 -0.02 1.05])