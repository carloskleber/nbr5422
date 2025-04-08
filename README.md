# NBR 5422

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10696412.svg)](https://doi.org/10.5281/zenodo.10696412)

Metodologia da norma ABNT NBR 5422:2024 "Projeto de linhas aéreas de energia elétrica - Critérios técnicos"

Rotinas em Matlab/ Octave e Python das fórmulas, para conferência e demonstração dos conceitos apresentados.

## Introdução

Este repositório foi utilizado durante a revisão da norma ABNT NBR 5422, e com sua publicação em 2024, servirá como meio de divulgação e discussão. Um dos objetivos é a comparação da NBR 5422:2024 com a versão anterior e outras metodologias, tais como IEC, IEEE e EN.

Este repositório não substitui o texto original da norma e não tem relação direta com a ABNT. A NBR 5422 pode ser obtida em https://www.abntcatalogo.com.br/pnm.aspx?Q=R2hENVV5YXEvQ2todGFyaWlScWtsR3d5WHBEdEpWV1VlVVhhd1lQS2trND0=

## Instalação

Aplica-se o procedimento usual em Python:
* Criar ambiente virtual: `python -m venv .venv`
* Entrar no ambiente virtual: `source .venv/bin/activate`
* Baixar os requisitos: `pip install -r requirements.txt`

## Utilização

Esta versão é dividida em duas partes: as bibliotecas, que contém as fórmulas da norma, e os demos, implementados em notebooks iPython (Jupyter) para uma melhor apresentação e interatividade.

Nas bibliotecas também serão implementadas outras normas, no qual poderão ser feitas comparações a partir de um mesmo projeto base.

## Guia de aplicação

O [Guia de aplicação](guiaAplicacao.pdf) é um texto didático para a utilização da NBR 5422 e textos correlatos, explicando a filosofia dos critérios e exemplificando algumas situações de projeto.

Este guia, assim como este repositório, é de uso aberto, aonde contribuições são bemvindas. O texto, até que seja dito ao contrário, é _work in progress_! Caso o utilize em algum estudo favor referenciar como:

    (autores). NBR 5422:2024 - Guia de Aplicação, v.x, (data de release). Disponível em https://github.com/carloskleber/nbr5422. Acesso em: (data de acesso).

# Licença

O repositório está sob a licença GPL 3.0, cuja tradução pode ser vista em: http://licencas.softwarelivre.org/gpl-3.0.pt-br.pdf

O repositório não tem qualquer afiliação com a ABNT.

Caso tenha encontrado qualquer violação de propriedade intelectual, entre em contato.

# Roadmap

* Comparar com outras normas e a versão 1985 da NBR 5422.
* Testar novas propostas para as próximas revisões.
* Priorizar a implementação Python por conter mais recursos open source.
* Implementar exemplos para uma gama representativa de projetos.

