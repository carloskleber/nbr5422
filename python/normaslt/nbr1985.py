#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, exp, log, sqrt
from normaslt import types
"""
Biblioteca de funções NBR 5422:1985
"""

def massaAr(alt:float, t:float) -> float:
  """
  Massa específica do ar - seção 8.2.1.1
  """
  return 1.293 / (1 + 0.00367 * t) * (16000 + 64 + t - alt)/(16000 + 64 + t + alt)

def correcaoVentoRetorno(v) -> float:
  """
  Correção da velocidade de vento obtida para um tempo de retorno especificado
  
  n - número de anos de coleta de dados
  t - período de retorno
  vm - velocidade média
  ktn - valor de frequência
  alfa - parâmetro de localização da distribuição de Gumbel
  beta - parâmetro de forma da distribuição de Gumbel  
  """

  """
  i = 1:n
  zi = -log(-log(i/(n+1)))
  c1 = 1/n * sum(zi)
  c2 = 1/sqrt(n) * sum(zi^2 - zm^2)
  ct = -log(-log(1+1/t))
  ktn = (c2-ct)/c1
  alfa = c1/s
  beta = vm - c2/s
  """

def anguloBalanco(v:float, q0:float, d:float, pcond: float, Vv:float, Vp:float) -> float:
  """
  Ângulo de balanço
  Seção 8.9.1
  """
  if v < 10:
    k = 1.0
  else:
    k = 3.68 * exp(-0.163*v) + 0.3
  return atan2(k *q0 * d * Vv, pcond * Vp)

def distHorizFF(du: float) -> float:
  """
  Distância horizontal entre fases no suporte - método convencional
  Seção 10.2.1 - tabela 4

  Válido entre fases de mesmo circuito ou circuitos diferentes, sendo
  Du = diferença fasorial das tensões entre os dois circuitos.
  """
  f = 60.
  d1 = 0.22 + 0.01 * du
  d2 = 0.37 * sqrt(f) + 0.0076 * du
  return max(d1, d2) 

def distHorizFFAlt(v:float, pu:float) -> float:
  """
  Distância horizontal entre fases no suporte - método alternativo
  Seção 10.2.2
  """
  a = 1.15
  b = 1.03
  k = 1.40
  return (v * pu * a / (500 * k))**1.667 * b

def distVertFT(du:float, obs:types.obs) -> float:
  """
  Distância mínima do condutor ao solo ou obstáculos - método convencional
  Seção 10.3.1

  du = Valor numericamente igual a tensão máxima de operação em kV
  obs = Tipo de obstáculo (enumeração)
  """
  match obs: # Tabela 5
    case types.obs.PEDESTRE:
      a = 6.
    case types.obs.RODOVIA:
      a = 8.
    case types.obs.LINHA_TRANSMISSAO:
      a = 1.2
    case _:
      a = 0. 
  if (du <= 87.):
    return a
  else:
    return a + 0.01 * (du/sqrt(3) - 50)
  
def distVertFTAlt(du:float, vl:float, pu:float, obs:types.obs) -> float:
  """
  Distância mínima do condutor ao solo ou obstáculos - método alternativo
  Seção 10.3.2

  du = Valor numericamente igual a tensão máxima de operação em kV
  vl = Valor numericamente igual a tensão máxima de crista para a terra
       em kV da linha de tensão menos elevada
  pu = Valor da sobretensão de manobra em pu de crista da tensão máxima
       de operação entre fase e terra, probabilidade de 98% de não ser excedido.
  obs = Tipo de obstáculo (enumeração)
  """
  match obs: # Tabela 6
    case types.obs.PEDESTRE:
      a1 = 2.8
      c = 1.2
      k = 1.15
    case types.obs.LINHA_TRANSMISSAO:
      a1 = 0.
      c = 1.2
      k = 1.4
    case _:
      a1 = 0.
      c = 1.
      k = 1.
  a2 = 1.15
  b = 1.03  
  return a1 + ((sqrt(2*du/3) * pu * vl) * a2 / (500. * k))**1.667 * b * c
