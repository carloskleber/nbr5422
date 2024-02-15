# NBR 5422

Metodologia da norma ABNT NBR 5422:2024 "Projeto de linhas aéreas de energia elétrica - Critérios técnicos"

Rotinas em Matlab/ Octave e Python das fórmulas, para conferência e demonstração dos conceitos apresentados.

## Introdução

Este repositório foi utilizado durante a revisão da NBR 5422, e com sua publicação em 2024, servirá como meio de divulgação e discussão. Um dos objetivos é a comparação da NBR 5422:2024 com a versão anterior e outras metodologias, tais como IEC, IEEE e EN.

Este repositório não substitui o texto original da norma, mas sim para elucidar a sua aplicação. A NBR 5422 pode ser obtido na ABNT: https://www.abntcatalogo.com.br/pnm.aspx?Q=R2hENVV5YXEvQ2todGFyaWlScWtsR3d5WHBEdEpWV1VlVVhhd1lQS2trND0=

## Utilização

Chamar a rotina principal especificando o caso de teste:

        nbr5422 teste1

Nos subdiretórios estão normas para comparação, que utilizam a mesma chamada:

        nbr1985 teste1
        iec teste1
        ieee teste1

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
* graficoKafl.m - Demonstração da variação de kafl para alguns parâmetros
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

* ampacidadeCigre.m - modelo ampacidade Cigre (conforme REN ANEEL 905 2020).

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

# Roadmap

* Comparar com outras normas e a versão 1985 da NBR 5422.
* Testar novas propostas para as próximas revisões.
* Eventualmente converter as rotinas para Python.