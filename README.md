# NBR 5422

Metodologia em discussão na revisão da norma NBR 5422 "Projeto de linhas aéreas de energia elétrica - Critérios técnicos"

Rotinas em Matlab/ Octave e Python das fórmulas, para conferência e demonstração dos conceitos apresentados.

## Relação das rotinas com as seções propostas

* nbr5422.m - Aplicação de todos os parâmetros de projeto. Utilizado na chamada dos testes principais (teste#.m)

### Seção 4

* dra.m - Cálculo da densidade relativa do ar (4.5.1)
* estatVento.m - Cálculo dos parâmetros estatísticos do vento (media e desvio padrao) por distribuição de Weibull.
* fatCorrAlt.m
* fatCorrRug.m
* fatorAtmFrenteLenta.m
* fatorUmidadeCA.m
* fatorUmidadeCC.m
* fatTurb.m
* massaAr.m
* umidAbs.m
* velVentoZ.m

### Seção 6

* readCapOper.m - Leitura do arquivo veraoDia.csv

### Seção 7

* distHoriz.m
* distVert.m

### Seção 8

* anguloNBR1985.m
* arrastoCabos.m
* fatorCxt1.m
* fatorCxt2.m
* fatorCxtc.m
* fatorEfetividadeVento.m
* fatorVentoCabo.m
* fatorVentoSuporte.m
* fatorVentoVao.m
* graficoCxt1.m
* graficoCxt2.m
* graficoGc.m
* graficoGl.m
* graficoGl.png
* graficoGtCadeia.m
* graficoKv.m

### Seção 9 

* espacFFFrenteLenta.m - Espaçamento fase-fase, frente lenta (9.4.2.4)
* espacFFFreqFund.m - Espaçamento fase-fase, frequência fundamental (9.3.3.1)
* espacFTFrenteLenta.m - Espaçamento fase-terra, frente lenta (9.4.1.1)
* espacFTFreqFund.m - Espaçamento fase-terra, frequência fundamental (9.3.2.1)
* espacFTFrenteRapida.m - Espaçamento fase-terra, frente rápida (9.5)

### Anexo A

* correcaoVentoRetorno.m
* pdfGumbel.m

Basear na planilha Excel

### Anexo C

* Risco_Kcs.py - gerador antigo da figura C-1
* Risco_KCs2.py - gerador atual, com figuras individuais

### Auxiliares (modelos e métodos fora da norma)

* TODO: modelo ampacidade Morgan.

### Depreciados

* distVegetacao.m
* fatK3s.m
* kIntJISF.m
* kIntNovo.m
* fatorCorrTint.m

## Rotinas de teste

* deducaoDU50.m
* teste1.m - Primeiro teste de projeto completo de linha.
* testeDU50.m - teste da derivação da fórmula de DU50.
* testeFatorAtmFL.m
* testeINMET.m - Teste de tratamento de dados do banco INMET (somente Matlab)
* testeJulian.m

# Bibliotecas e bases de dados externas

* INMET: https://portal.inmet.gov.br/dadoshistoricos