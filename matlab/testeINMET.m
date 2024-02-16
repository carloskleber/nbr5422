%% Teste de tratamento de dados do banco INMET
close all

t1 = dadosINMET('../inmet/INMET_NE_PE_A301_RECIFE_01-01-2016_A_31-12-2016.CSV');
t2 = dadosINMET('../inmet/INMET_NE_PE_A301_RECIFE_01-01-2017_A_31-12-2017.CSV');
t3 = dadosINMET('../inmet/INMET_NE_PE_A301_RECIFE_01-01-2018_A_31-12-2018.CSV');
t4 = dadosINMET('../inmet/INMET_NE_PE_A301_RECIFE_01-01-2019_A_31-12-2019.CSV');
t5 = dadosINMET('../inmet/INMET_NE_PE_A301_RECIFE_01-01-2020_A_31-12-2020.CSV');
t6 = dadosINMET('../inmet/INMET_NE_PE_A301_RECIFE_01-01-2021_A_31-12-2021.CSV');

vHor = [t1.vHor; t2.vHor; t3.vHor; t4.vHor; t5.vHor; t6.vHor];
% identificadores de dia
idDia = [(t1.hora > 5 & t1.hora < 18); (t2.hora > 5 & t2.hora < 18); (t3.hora > 5 & t3.hora < 18); (t4.hora > 5 & t4.hora < 18); (t5.hora > 5 & t5.hora < 18); (t6.hora > 5 & t6.hora < 18)];
vHorD = vHor(idDia);
vHorN = vHor(~idDia);

vHor = vHor(vHor ~= -9999);
vHor = vHor(~isnan(vHor));
figure
histogram(vHor,'BinLimits',[0.05 5.05],'BinWidth',0.1,'normalization','pdf');
xlabel('Vento horario (m/s)')

vHorD = vHorD(vHorD ~= -9999);
vHorD = vHorD(~isnan(vHorD));
figure
histogram(vHorD,'BinLimits',[0.05 5.05],'BinWidth',0.1,'normalization','pdf');
xlabel('Vento horario, dia (m/s)')

vHorN = vHorN(vHorN ~= -9999);
vHorN = vHorN(~isnan(vHorN));
figure
histogram(vHorN,'BinLimits',[0.05 5.05],'BinWidth',0.1,'normalization','pdf');
xlabel('Vento horario, noite (m/s)')
figure 
ecdf(vHor, 'function','survivor');
hold on
ecdf(vHorD, 'function','survivor');
ecdf(vHorN, 'function','survivor');
xlabel('Vento horario (m/s)');
hold off
legend('Total', 'Dia', 'Noite');

tArSeco = [t1.tArSeco; t2.tArSeco; t3.tArSeco; t4.tArSeco; t5.tArSeco; t6.tArSeco];
tArSeco = tArSeco(tArSeco ~= -9999);
tArSeco = tArSeco(~isnan(tArSeco));
figure
histogram(tArSeco,'BinWidth',1,'normalization','pdf');
xlabel('Temperatura do ar, bulbo seco (oC)')
figure 
ecdf(tArSeco, 'function','survivor');
xlabel('Temperatura do ar, bulbo seco (oC)');