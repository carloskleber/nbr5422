#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, cos, exp, sin, pi
"""
Biblioteca de funções "em trabalho"
"""
def anguloBalanco(v:float, d:float, ncond:int, pcond:float, piso:float, aiso:float, Lm:float, Lp:float, T:float) -> float:
  """Fórmula proposta para ângulo de balanço

  Argumentos:
  v -- velocidade do vento em m/s referida a 30 s
  d -- diâmetro do cabo em m
  ncond -- número de subcondutores
  pcond -- peso linear por subcondutor em N/m
  piso -- peso da cadeia de isoladores em N
  aiso -- area exposta de cadeia de isoladores em m²
  Lm -- vão médio (ou de vento) em m
  Lp -- vão gravante (ou de peso) em m
  T -- tração por subcondutor em N
  """

  # Ângulo de ataque do vento
  beta = 0.5*pi
  # ângulo de deflexão no suporte
  theta = 0
  # Correção empírica do ângulo - NBR 5422:1985
  if v < 10:
    k = 1.0
  else:
    k = 3.68 * exp(-0.163*v) + 0.3
  q0 = 0.5 * 1.225 * v**2
  # Coeficiente de efetividade - IEC 60826
  gl = 4e-10 * Lm**3 -5e-7 * Lm**2 -1e-4 * Lm + 1.0403
  qcond = q0 * gl * ncond * d * Lm * sin(beta)**2 * cos(0.5 * theta)
  qiso = q0 * 1.2 * aiso
  # Esforço devido ao ângulo de deflexão
  qdef = 2 * ncond * T * sin(0.5 * theta)
  pcond = ncond * pcond * Lp
  return atan2(k * qcond + 0.5 * qiso + qdef, pcond + 0.5 * piso)

def anguloHornisgrinde(v:float, d:float, pcond: float, Lm:float, Lp:float) -> float:
  """Fórmula de ângulo de balanço de Hornisgrinde
  Ref.: Furnas, Transitórios Elétricos e Coordenação de Isolamento, EDUFF, 1987, p. 283
  Baseado em MORS, H. Wind pressure on overhead transmission line conductors - Hornisgrinde
  Testing Station, Report 220, Cigre, Paris, 1956.
  """
  if v< 15:
    k = 1.
  else:
    k = 9.787026460005688 * exp(-v * 0.21214059279219613) +0.610802908689377
  return atan2(0.05832 * v**2 * k * d * Lm, pcond * Lp)