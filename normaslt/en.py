#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import exp, sqrt
from normaslt import types
"""
Biblioteca de funções EN 50341-1:2012
Baseado na IEC 60071-1, IEC 60071-2 e Cigre Brochure 72
"""
def fatorCorrAlt(h:float, m=1.) -> float:
  """
  Fator de correção de altitude
  h = altitude em m
  m = expoente relativo ao tipo de sobretensão
  """
  return exp(m * h / 8150.)

def espacPowerFreqEL(us:float, ka:float, kg:float, kz=0.91) -> float:
  """
  Cálculo da distância para frequência industrial, fase-terra
  Table E.5 (p. 165)
  us = Highsest system voltage in kV rms
  """
  kgpf=1.35*kg-0.35*kg**2
  return ((exp(us/(750.*sqrt(3)*ka*kz*kgpf))-1.)/0.55)**0.83

def espacPowerFreqPP(us:float, ka:float, kg:float, kz=0.91) -> float:
  """
  Cálculo da distância para frequência industrial, fase-terra
  Table E.5 (p. 165)
  us = Highsest system voltage in kV rms
  """
  kgpf=1.35*kg-0.35*kg**2
  return ((exp(us/(750.*ka*kz*kgpf))-1.)/0.55)**0.83

def espacSlowFrontEL(ue2:float, kcs:float, ka:float, kg:float, kz=0.922) -> float:
  """
  Cálculo da distância para sobretensões de frente lenta, fase-terra
  Table E.5 (p. 165)
  ue2 = overvoltage phase to earth stressing the air gap with prob. of 2% to be exceeded
  kcs = coordination statistical factor
  """
  return 1/0.46 * (exp(kcs*ue2/(1080. * ka * kz * kg))-1.)

def espacSlowFrontPP(ue2:float, kcs:float, ka:float, kg:float, kz=0.922) -> float:
  """
  Cálculo da distância para sobretensões de frente lenta, fase-fase
  Table E.5 (p. 165)
  ue2 = overvoltage phase to earth stressing the air gap with prob. of 2% to be exceeded
  """
  return 1/0.46 * (exp(1.4*kcs*ue2/(1080. * ka * kz * kg))-1.)

def espacFastfrontEL(u90:float, ka:float, kg:float, kz=0.961) -> float:
  """
  Cálculo da distância para sobretensões de frente rápida, fase-terra
  Table E.5 (p. 165)
  """
  kgff = 0.74 + 0.26 * kg
  return u90/(530. * ka * kz * kgff)

def espacFastfrontPP(u90:float, ka:float, kg:float, kz=0.961) -> float:
  """
  Cálculo da distância para sobretensões de frente rápida, fase-fase
  Table E.5 (p. 165)
  """
  kgff = 0.74 + 0.26 * kg
  return 1.2 * u90/(530. * ka * kz * kgff)
