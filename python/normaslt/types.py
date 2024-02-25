#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum, auto
"""
Biblioteca de tipos aplicáveis as normas
"""

class rug(Enum):
      """
      Classe de rugosidade do terreno
      """
      A = auto()
      B = auto()
      C = auto()
      D = auto()

class obs(Enum):
      """
      Tipo de obstáculos para distâncias verticais e horizontais
      Tabelas 5 e 7
      """
      PEDESTRE = "acesso somente a pedestres"
      EDIFICACAO = "edificação"
      RODOVIA = "rodovia"
      FERROVIA_NAO_ELETRIFICADA = "ferrovia não eletrificada"
      FERROVIA_ELETRIFICADA = "ferrovia eletrificada"
      VEGETACAO_PERM = "vegetação de preservação permanente"
      MAQ_AGRICOLA = "máquinas agrícolas"
      SUPORTE_FERROVIA = "suporte de linha pertencente à ferrovia"
      AGUAS_NAVEGAVEIS = "águas navegáveis"
      AGUAS_NAO_NAVEGAVEIS = "águas não navegáveis"
      LINHA_TRANSMISSAO = "linha de energia elétrica"
      LINHA_TELECOM = "linha de telecomunicações"
      CULT_AGRIC_PERM = "cultura agrícola permanente"
      INSTALACAO_TRANSP = "instalação transportadora"

class gap(Enum):
      """
      Tipos de gap
      Baseado na NBR 8186:2021, tanto fase-terra quando fase-fase
      """
      CONDUTOR_BRACO = "condutor - braço de torre"
      CONDUTOR_JANELA = "condutor - janela"
      CONDUTOR_PLANO_ABAIXO = "condutor - plano abaixo"
      CONDUTOR_HASTE_ABAIXO = "condutor - haste abaixo"
      CONDUTOR_ESTRUTURA_LATERAL = "condutor - estrutura lateral"
      ESTRUTURA_HASTE = "Estrutura - haste"
      CONDUTOR_ESTAI = "condutor - estai"
      ANEL_ANEL = "anel - anel"
      CONDUTOR_CRUZADO = "condutores cruzados"
      CONDUTOR_PARALELO = "condutores paralelos"
      BARRAMENTO = "barramentos suportados por isolador"
      ASSIMETRICO = "geometria assimétrica"

class regiao(Enum):
      """
      Região geográfica
      """
      CO = auto()
      N = auto()
      NE = auto()
      S = auto()
      SE = auto()

class tensao(Enum):
      """
      Classes de tensão conforme NBR 6939
      Utilizando valores nominais usuais
      """
      _15kV = (13.8, 15.)
      _24_2kV = (23.1, 24.2)
      _36_2kV = (34.5, 36.2)
      _72_5kV = (69., 72.5)
      _92_4kV = (88., 92.4)
      _145kV = (138., 145.)
      _242kV = (230., 242.)
      _362kV = (345., 362.)
      _460kV = (440., 460.)
      _550kV = (500., 550.)
      _800kV = (765., 800.)

      def nom(v) -> float:
            # Valor nominal
            return v.value[0]
      
      def max(v) -> float:
            # Valor máximo
            return v.value[1]

class amp(Enum):
      """
      Estados de regime e condições de referência
      """
      TIPICA_NOMINAL = ("tip,n", "Condição típica, regime nominal")
      TIPICA_SOBRECORRENTE = ("tip,s", "Condição típica, regime sobrecorrente")
      LIMITE_NOMINAL = ("lim,n", "Condição limite, regime nominal")
      LIMITE_SOBRECORRENTE = ("lim,s", "Condição limite, regime sobrecorrente")

      def suf(v) -> str:
            # Sufixo
            return v.value[0]
      
      def desc(v) -> str:
            # Texto descritivo
            return v.value[1]
