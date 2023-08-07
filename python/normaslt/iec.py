#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import exp, sqrt
from normaslt import types
"""
Biblioteca de funções IEC 60071-2:2018
"""
def fatorCorrAlt(h:float, m=1.) -> float:
  """
  Fator de correção de altitude
  Sec. 6.2.2
  h = altitude em m
  m = expoente relativo ao tipo de sobretensão (vide fig. 9)
  """
  return exp(m * h / 8150.)

def espacPowerFreq(k:float, u50rp=-1., un=-1., ftmo=1., fca=1., sigma=0.03) -> float:
  """
  Cálculo da distância a partir da referência ponta-plano
  Eq. F-1: U50rp = 750 * sqrt(2) * log(1 + 0.55 * d**1.2)
  Deve-se utilizar um dos seguintes argumentos:
  u50rp = 50% breakdown voltage for a rod-plane gap, kV crest
  un = tensão nominal em kV (de linha ou de fase, de acordo com o espaçamento estudado).
    Caso un seja utilizado, aplica-se também:
    ftmo = Fator da tensão máxima de operação em pu
    fca = Fator de correção atmosférico
    sigma = desvio padrão
  *** Valid for gaps up to 3 m
  For gaps larger than 2 m, the strength can be evaluated with:
  Eq. F-2: U50 = U50rp * (1.35 * K - 0.35 * K**2)
  K = Gap factor (table F-1)
  """
  if un != -1.:
    u50rp = un * ftmo * sqrt(2) /(sqrt(3)*(1-3*sigma)*fca)
  if u50rp == -1.:
    raise("Necessário definir un ou u50rp.")

  d = 1.6458 * (exp(u50rp/(750 * sqrt(2)))-1)**0.8333
  if (d > 2):
    u50 = u50rp * (1.35 * k - 0.35 * k**2)
    d = 1.6458 * (exp(u50/(750 * sqrt(2)))-1)**0.8333
  return d

def espacSlowFront(u50rp:float, k:float) -> float:
  """
  Cálculo da distância para sobretensões de frente lenta
  Eq. F-3 e F-5: k * U50rp = 1080 log(0.46 * d + 1)
  u50 = 50% breakdown voltage for a rod-plane gap, kV crest
  """
  return 2.1739 * (exp(k * u50rp / 1080.) - 1.)

def espacFastfront(u50rp:float, k:float) -> float:
  """
  Cálculo da distância para sobretensões de frente rápida
  Eq. 
  u50 = 50% breakdown voltage for negative polarity, kV crest
  Válido para gaps entre 1 e 10 m
  """
  kff = 0.74 + 0.26 * k
  return kff * u50rp / 530.