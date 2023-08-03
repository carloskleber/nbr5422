#!/usr/bin/python
# -*- coding: utf-8 -*-
from enum import Enum

class rug(Enum):
      """
      Classe de rugosidade do terreno
      """
      A = 0
      B = 1
      C = 2
      D = 3

class obs(Enum):
      """
      Tipo de obstáculos para distâncias verticais e horizontais
      """
      PEDESTRE = 0
      EDIFICACAO = 1
      RODOVIA = 2
      FERROVIA_NAO_ELETRIFICADA = 3
      FERROVIA_ELETRIFICADA = 4
      VEGETACAO_PERM = 5
      MAQ_AGRICOLA = 6
      SUPORTE_FERROVIA = 7
      AGUAS_NAVEGAVEIS = 8
      AGUAS_NAO_NAVEGAVEIS = 9
      LINHA_TRANSMISSAO = 10
      LINHA_TELECOM = 11
      CULT_AGRIC_PERM = 12
      INSTALACAO_TRANSP = 13

class gap(Enum):
      """
      Tipos de gap
      """
      CONDUTOR_BRACO = 0
      CONDUTOR_JANELA = 1
      CONDUTOR_PLANO_ABAIXO = 2
      CONDUTOR_HASTE_ABAIXO = 3
      CONDUTOR_ESTRUTURA_LATERAL = 4
      ESTRUTURA_HASTE = 5
      ANEL_ANEL = 6
      CONDUTOR_CRUZADO = 7
      CONDUTOR_PARALELO = 8
      BARRAMENTO = 9
      ASSIMETRICO = 10

class regiao(Enum):
      """
      Região geográfica
      """
      CO = 0
      N = 1
      NE = 2
      S = 3
      SE = 4

class tensao(Enum):
      """
      Classes de tensão conforme NBR 6939
      Utilizando valores nominais usuais
      """
      _15kV: (13.8, 15.)
      _24_2kV: (23.1, 24.2)
      _36_2kV: (34.5, 36.2)
      _72_5kV: (69., 72.5)
      _92_4kV: (88., 92.4)
      _145kV: (138., 145.)
      _242kV: (230., 242.)
      _362kV: (345., 362.)
      _460kV: (440., 460.)
      _550kV: (500., 550.)
      _800kV: (765., 800.)

      @classmethod
      def nom(v) -> float:
            return v.value[0]
      
      @classmethod
      def max(v) -> float:
            return v.value[1]

      