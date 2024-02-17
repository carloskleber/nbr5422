# NBR 5422:2024 - Guia de Aplicação

## Introdução

A norma NBR 5422 apresenta uma série de critérios para assegurar a qualidade de um projeto, porém não é um texto didático.

Este texto, inspirado em publicações semelhantes, procura esclarecer a aplicação da norma.

## Dados básicos

Um projeto de linha pressupõe uma proposta inicial, com tensão, correntes e geometria de suportes e cabos, além de um traçado, no qual se implica nos dados de terreno e climatológicos. 

A finalidade neste ponto é chegar a um projeto básico - um perfil de torre típica. O projeto executivo 

Cabe observar que a NBR 5422 não se aplica somente a linhas de transmissão do Sistema Interligado Nacional (SIN) - assim como na sua versão anterior, a norma vale para qualquer linha aérea com tensão nominal acima de 38 kV.

## Referências complementares

Para a devida aplicação da NBR 5422 no projeto de uma linha, outras referências devem ser aplicadas:

* Uma base de dados meteorológicos, como INMET (https://portal.inmet.gov.br/dadoshistoricos)
* Um modelo de cálculo de flecha, como por exemplo do Cigre (Cigre WG 22.12, "The thermal behaviour of overhead conductors", Electra 144, 1992), conforme adotado pela REN ANEEL 905 de 2020, Anexo II (revoga REN 191 2005).

## Fluxo de trabalho

A concretização de um projeto de linha aérea passa por algumas etapas. Especificamente na transmissão do Sistema Interligado Nacional (SIN), algumas etapas são realizadas pela EPE através de seus relatórios técnicos.

1. Planejamento da transmissão (Relatório R1 EPE)
2. Estudos elétricos (Relatório R2 EPE)
3. Definição preliminar da rota e impacto socioambiental (Relatório R3 EPE)
4. Custos fundiários (Relatório R5 EPE) e compartilhamento de instalações (Relatório R4 EPE)
5. Licenciamento
6. Definição final da rota
7. Construção
8. Energização

## Metodologia

### Segurança do projeto

Definições de risco de falha de um projeto

### Elementos solicitantes

Histórico - Labegalini (p. 97)

Ver artigos recentes

### Elementos meteorológicos (seção 4 e Anexo A)

Tratamento de dados

### Temperatura do condutor (seções 5, 6 e 21, Anexo B)

Cálculo das temperaturas no condutor para cada risco térmico, associada a uma distribuição estatística.

As figuras do Anexo B foram geradas a partir de um exemplo processado pelo Claudionor. A ideia é ter no futuro uma rotina interna calculando a temperatura, para uma dada locação (vinculada a uma base de dados INMET).

A partir do risco térmico, extrai-se as temperaturas para 15%, 5% e 1%, para serem associadas as distâncias de segurança.

As correntes podem ser estabelecidas para cada período climático - mas isso já seria implícito no cálculo geral? No final haverá uma temperatura/ distância determinante do projeto.

### Distâncias de segurança (seção 7)

* Distâncias verticais
* Definição da altura básica do suporte

### Ação mecânica do vento (seção 8)

Cálculo dos ângulos de balanço.

### Projeto de isolamento (seção 9 e Anexo C)

Distâncias minímas fase-terra e entre fases.

### Projeto mecânico de cabos, suportes e fundações (seções 11, 12 e 13)

Critérios e hipóteses de carregamento.

### Faixa de passagem (seções 10, 17 e 18)

Cálculo da largura de faixa por critérios elétricos (seção 10) e mecânicos (balanço)

Os critérios elétricos podem ser divididos em fenômenos lineares (campo elétrico e magnético) e os relativos ao efeito corona (ruído audível e radiointerferência). O cálculo dos campos elétrico e magnético podem ser obtidos pelas equações do eletromagnetismo, considerando respectivamente os potenciais e correntes na linhas nas condições operativas máximas, além da sua posição geométrica mais provável (notadmente, as flechas).

Os fenômenos oriundos do efeito corona podem ser obtidos por modelos empíricos. O modelo seminal foi desenvolvido por Peek, no qual determina o campo elétrico crítico em um cilindro, em kV/cm:

$$E_c = 30 \delta m \left( 1 + \frac{0,3}{\sqrt{\delta \, r}} \right)$$

### Projeto executivo

* Projeto de travessias (seção 20)
* Aplicação de vento de projeto (seção 4) no cálculo detalhado.
* Manutenção de faixa de passagem (seção 19)

## Referências

* Fuchs, R.D. 
* Labegalini, P.R., Labegalini, J.A., Fuchs, R.D. e Almeida, M.T. Projetos mecânicos das linhas aéreas de transmissão. 2ª edição, Editora Blucher, 1992.
* Power Line Systems. Proposed workflow for PLS-CADD, https://www.powline.com/technotes/PLS-CADD_Workflow.pdf