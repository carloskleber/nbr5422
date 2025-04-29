#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, exp, log, pi, radians, sin, sqrt
from normaslt import types
"""Biblioteca de funções NBR 5422:1985
"""

def massaAr(alt:float, t:float) -> float:
  """Massa específica do ar - seção 8.2.1.1
  """
  return 1.293 / (1 + 0.00367 * t) * (16000 + 64 + t - alt)/(16000 + 64 + t + alt)

def correcaoVentoPeriodoRetornoSecao4(alfa, beta, T) -> float:
  """Correção da velocidade de vento obtida para um tempo de retorno especificado
  De acordo com Seção 4.8.2
  Os parâmetros de distribuição de Gumbel referem-se a um período de retorno de 50 anos.

  :param alfa: Parâmetro de localização (ou estimador do fator de escala) da distribuição de Gumbel
  :param beta: Parâmetro de forma (ou estimador do fator de posição) da distribuição de Gumbel
  :param T: Período de retorno
  """
  return beta - (log(-log(1 - 1/T)))/alfa

def correcaoVentoPeriodoRetornoAnexoC(vb:float, T:float, Vmed:float, sigmaV: float) -> float:
  """Correção do vento de projeto para um período de retorno
  De acordo com Seção C.3

  :param vb: Velocidade de projeto para tempo de retorno de 50 anos
  :param Vmed: Valor médio das velocidades de vento máxima anuais registradas durante n anos
  :param sigmaV: Desvio padrão das velocidades registradas
  """
  d = sigmaV/ Vmed
  a = 1 - 0.45 * d
  b = sqrt(6)/ pi * d
  c = 1 + 2.59 * d
  vt = vb * (a + b*(-log(-log(1 - 1/T))))/ c
  return T


def anguloBalanco(v: float, q0: float, d: float, pcond: float, Lm=1., Lp=1., VpVv=-1.) -> float:
  """Cálculo de ângulo de balanço
  Seção 8.9.1

  :param v: Velocidade do vento referida a 30 s (m/s)
  :param q0: Pressão dinâmica (Pa)
  :param d: Diâmetro do cabo (m)
  :param pcond: Peso linear do cabo (N/m)
  :param Lm: Vão médio (ou de vento) (m)
  :param Lp: Vão gravante (ou de peso) (m)
  :param VpVv: Relação vão de peso por vão de vento
  """
  if VpVv == -1:
    VpVv = Lp/Lm

  if v < 10:
    k = 1.0
  else:
    k = 3.68 * exp(-0.163*v) + 0.3
  return atan2(k * q0 * d, pcond * VpVv)

def anguloBalancoDeflexao(v: float, q0: float, d: float, pcond: float, theta: float, T: float, Lm: float, Lp: float) -> float:
  """Ângulo de balanço considerando deflexão na estrutura
  Adaptado da fórmula original

  :param v: Velocidade do vento referida a 30 s (m/s)
  :param q0: Pressão dinâmica (Pa)
  :param d: Diâmetro do cabo (m)
  :param pcond: Peso linear do cabo (N/m)
  :param theta: Ângulo de deflexão (graus)
  :param T: Tração (N)
  :param Lm: Vão médio (ou de vento) (m)
  :param Lp: Vão gravante (ou de peso) (m)
  """

  if v < 10:
    k = 1.0
  else:
    k = 3.68 * exp(-0.163*v) + 0.3
  return atan2(k * (q0 * d * Lm + 2 * T * sin(0.5 *radians(theta))), pcond * Lp)

def distHorizFF(du: float, f: float) -> float:
  """
  Distância horizontal entre fases no suporte - método convencional
  Seção 10.2.1 - tabela 4

  Válido entre fases de mesmo circuito ou circuitos diferentes, sendo
  :param Du: Diferença fasorial das tensões entre os dois circuitos (kV).
  :param f: Flecha 
  """
  d1 = 0.22 + 0.01 * du
  d2 = 0.37 * sqrt(f) + 0.0076 * du
  return max(d1, d2) 

def distHorizFFAlt(v:float, pu:float, a=1.15, b=1.03, k=1.40) -> float:
  """
  Distância horizontal entre fases no suporte - método alternativo
  Seção 10.2.2
  :param v: valor de crista entre fases (kV)
  :param pu: Sobretensão de manobra (pu crista), para probabilidade 98% de não ser excedido
  """
  return (v * pu * a / (500 * k))**1.667 * b

def distVertFT(du:float, obs=types.obs.PEDESTRE) -> float:
  """
  Distância mínima do condutor ao solo ou obstáculos - método convencional
  Seção 10.3.1

  du = Valor numericamente igual a tensão máxima de operação em kV
  obs = Tipo de obstáculo (enumeração)
  """
  if (du <= 87.):
    return a
  match obs: # Tabela 5
    case types.obs.PEDESTRE:
      a = 6.
    case types.obs.RODOVIA:
      a = 8.
    case types.obs.LINHA_TRANSMISSAO:
      a = 1.2
    case _:
      a = 0. 
  return a + 0.01 * (du/sqrt(3) - 50)
  
def distVertFTAlt(du:float, vl:float, pu:float, obs=types.obs.PEDESTRE) -> float:
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

def fatCorrAlt(alt: float, rug=types.rug.B) -> float:
  """Fator de correção da altura
  Seção ...
  """
  match rug:
    case types.rug.A:
      alfa = 0.110
    case types.rug.B:
      alfa = 0.160
    case types.rug.C:
      alfa = 0.220
    case types.rug.D:
      alfa = 0.280
    case _:
      warn("Classe de rugosidade inválida.")
  return (alt/10)**alfa

def fatCorrInt(t, rug=types.rug.B) -> float:
  """Fator de correção do período de integração
  Seção 4.8.3 - Figura 1

  OBS.: a figura na NBR não coincide em escala com a da IEC 60826 (convergindo para 10 min), apesar de ser a mesma referência.

  :param t: período de integração (s)
  :param rug: Categoria do terreno
  """
  match rug:
    case types.rug.A:
      return 1.17
    case types.rug.B:
      return -0.069 * log(t) + 1.4488 # ajuste de curva no Excel - confirmar se Kint(600) = 1
    case types.rug.C:
      return 1.30
    case types.rug.D:
      return 1.48
    case _:
      warn("Classe de rugosidade inválida.")