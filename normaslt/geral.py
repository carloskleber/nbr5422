#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import cosh, exp, log, pi, sin, sinh, sqrt
import numpy as np
from enum import Enum
from scipy.optimize import ridder

"""
Biblioteca geral de funções, não associadas a normas
"""
class Cabo:
  """
  Atributos:
  desc -- Denominação do cabo
  d -- diâmetro nominal em m
  S -- seção em m²
  p -- peso linear em N/m
  T -- tração de ruptura em N
  E -- módulo de elasticidade em N/m²
  alfa1 -- coeficiente de dilatação térmica em 1/°C
  tCA -- Temperatura de referência para resistência CA em °C
  rCA -- resistência CA para cada tCA em Ω/m
  """
  def __init__(self, desc, d, S, p, T, E, alfa1, tCA, rCA):
    self.desc = desc
    self.d = d
    self.S = S
    self.p = p
    self.T = T
    self.E = E
    self.alfa1 = alfa1
    self.tCA = tCA
    self.rCA = rCA

  def __str__(self):
    return self.desc

class dbCabo(Enum):
  """Banco de dados de cabos para usar nos exemplos
  """

  # DADOS PROVISORIOS - checar

  #               desc            d        S          p        T         E        alfa1    tCA                rCA
  CAA_LINNET   = ('CAA Linnet',   0.01831, 0.0001982, 6.75713,  62509.3, 7.26e10, 1.89e-5, [25, 50, 75, 100], [0.0001738, 0.0001909, 0.0002081, 0.0002252])
  CAA_GROSBEAK = ('CAA Grosbeak', 0.02515, 0.0003788, 12.7736, 111245.0, 7.26e10, 1.89e-5, [25, 50, 75, 100], [9.22E-05, 0.0001012, 0.0001103, 0.0001193])
  CAA_RAIL     = ('CAA Rail',     0.02959, 0.0005168, 15.694,  119702.0, 6.51e10, 2.07e-5, [25, 50, 75, 100], [6.24E-05, 6.83E-05, 7.43E-05, 8.02E-05])
  CAA_HAWK     = ('CAA Hawk',     0.02179, 0.000281,  9.6138,   86455.5, 7.26e10, 1.89e-5, [25, 50, 75, 100], [0.0001227, 0.0001348, 0.0001469, 0.0001589])
  CAA_ZEBRA    = ('CAA Zebra',    0.02858, 0.000482,  16.19,   133e3,    7.26e10, 1.89e-5, [25, 75, 100], [0.042e-3, 0.0524e-3, 0.0568e-3])
  CA_COREOPSIS = ('CA Coreopsis', 0.03693, 0.0008058, 2.22041, 120143.0, 5.85e10, 2.30e-5, [25, 50, 75, 100], [3.95E-05, 4.29E-05, 4.63E-05, 4.97E-05])
  CAL_CHLORINE = ('CAL Chlorine', 7.5e-3,  34.36e-6,  9.463,    8.16e3,   0, 0, [], [])
  CAL_SELENIUM  = ('CAL Selenium',29.25e-3, 506.04e-6,13.9364, 113.86e3,   0, 2.3e-5, [50, 100], [0.0679, 0.0679+50*0.0039]) # coef. 0.00390 /°C ref.: Prysmian
  CAL_OXYGEN   = ('CAL Oxygen',   23.75e-3,336.69e-6, 9.2725,  73.57e3,  0, 0, [], [])

  def __init__(self, desc, d, S, p, T, E, alfa1, tCA, rCA):
    self.desc = desc
    self.d = d
    self.S = S
    self.p = p
    self.T = T
    self.E = E
    self.alfa1 = alfa1
    self.tCA = tCA
    self.rCA = rCA

  def __str__(self):
    return self.desc

def flecha1(p, A, T) -> float:
  return p * A**2 / (8. * T)

def flecha2(p, A, T) -> float:
  return T/p * (cosh(A * p/ (2 * T)) - 1)

def equacaoEstado(p, A, T0, S, E, alfa1, t0, t1) -> tuple[float, float]:
  """Equação de estado de cabos

  Args:
  p -- peso unitário do condutor [N/ m]
  A -- comprimento do vão (horizontal) [m]
  T0 -- tração horizontal inicial [N]
  S -- seção transversal [mm²]
  E -- módulo de elasticidade [N/mm²]
  alfa1 -- coeficiente de dilatação térmica [1/°C]
  t0 -- temperatura inicial [°C]
  t1 -- temperatura final [°C]
  Returns:
  f -- flecha final [m]
  T2 -- tração final [N]

  TODO prever alteração no peso final (ex. força do vento)
  """
  
  if alfa1 == 0:
    raise ValueError('Coeficiente linear (alfa1) igual a zero.')
  deltat = t1 - t0
  if deltat == 0:
    T2 = T0
    f = flecha2(p, A, T2)
    return f, T2
  elif deltat > 0:
    T2i = 0.1 * T0
    T2f = T0
  else:
    T2i = T0
    T2f = 10. * T0
  invalfa = 1. / alfa1
  inves = 1. / (E * S)
  deltai = 0.
  deltaf = 1e7
  while abs(deltaf - deltai) > 1e-3:
    deltai = eqEstado(invalfa, T0, T2i, A, p, inves) - deltat
    deltaf = eqEstado(invalfa, T0, T2f, A, p, inves) - deltat
    T2med = 0.5 * (T2i + T2f)
    deltamed = eqEstado(invalfa, T0, T2med, A, p, inves) - deltat
    if (deltai*deltamed) <= 0:
      T2f = T2med
    else:
      T2i = T2med
  T2 = T2i
  f = flecha2(p, A, T2)
  return f, T2

def eqEstado(invalfa, t01, t02, a, p, inves) -> float:
  """Equação de estado - parte para iteração
  """
  c1 = t01 / p
  c2 = t02 / p
  return invalfa * ((c2*sinh(a/(2*c2)) / (c1*sinh(a/(2*c1))) - 1) -inves * (t02 - t01))

def ampacidadeCigre(temp: float, velVento, ataque, tempAr, radglobal, alt, cabo: dbCabo, rugcond=0.9, absorcao=0.93, emicond=0.95) -> float:
  """Calculo da relação entre temperatura e corrente em um condutor - método Cigre.
  Fonte: "The termal behaviour of overhead conductors, sec 1 and 2, WG 22.12, Electra 144 oct 1992"

  Args:
  temp -- temperatura de operação (°C, superior a temperatura ambiente)
  velVento -- velocidade do vento (m/s)
  ataque -- ângulo de ataque do vento (rad) (pi/2 = perpendicular ao cabo)
  tar -- temperatura do ar (°C)
  radglobal -- radiação solar (W/m²)
  alt -- altura do condutor (m)
  cabo -- Objeto cabo conforme base de dados de exemplo
  rugcond -- rugosidade do condutor
  absorcao -- coeficiente de absorção solar (0.3 para cabos brilhantes, 0.93 para cabos envelhecidos/poluidos)
  emicond -- taxa de emissividade (0.5 para oxidados, 0.95 envelhecidos, 0.96 molhados)

  Returns:
  corrente -- corrente no condutor (A)
  """
  dcond = cabo.d
  tempCAref = cabo.tCA
  rCAref = cabo.rCA
  gs = gSolar(absorcao, radglobal, dcond)
  pr = pRad(dcond, emicond, temp, tempAr)
  pc = CIGRE_PConv(velVento, ataque, tempAr, alt, temp, dcond, rugcond)
  if len(tempCAref) < 2:
  	raise ValueError('Dados insuficientes na tabela do cabo para determinação da resistência CA em função da temperatura.')	
  rac = np.interp(temp, tempCAref, rCAref)
  q = pr + pc - gs
  if q < 0:
    corrente = -sqrt(-q/rac)
  else:
    corrente = sqrt(q/rac)
  return corrente

def ampacidadeCigreMin(temp: float, amp: float, velVento, ataque, tempAr, radglobal, alt, cabo: dbCabo, rugcond=0.9, absorcao=0.93, emicond=0.95) -> float:
  a = amp - ampacidadeCigre(temp, velVento, ataque, tempAr, radglobal, alt, cabo, rugcond, absorcao, emicond)
  return a

def pRad(dcond, emicond, tcond, tar):
  return pi * dcond * 5.6697e-8 * emicond * ((tcond + 273)**4 - (tar + 273)**4)

def gSolar(absorcao, radglobal, dcond):
  return absorcao * radglobal * dcond

def CIGRE_PConv(vvnt, ataque, tar, alt, tcond, dcond, rugcond):
  tfilme = (tcond + tar) / 2
  dtemp = tcond - tar
  vf = 1.32e-5 + 9.5e-8 * tfilme #  viscosidade cinematica
  lf = 0.0242 + 7.2e-5 * tfilme # condutividade termica do filme de ar
  prandtl = 0.715 - 0.00025 * tfilme
  grashof = dcond**3 * 9.807 * dtemp / ((tfilme + 273) * vf**2)
  rayleigh = grashof * prandtl
  nusselt = CIGRE_PConvNatural(rayleigh)
  if vvnt != 0:
    ro_alt = exp(-0.000116 * alt)
    reynolds = ro_alt * vvnt * dcond / vf
    if vvnt >= 0.5:
      nusselt = CIGRE_PConvForcada(reynolds, ataque, rugcond)
    else:
      nusselt_a = CIGRE_PConvForcada(reynolds, pi/4, rugcond)
      nusselt_b = CIGRE_PConvForcada(reynolds, pi/2, rugcond)
      nusselt_b = 0.55 * nusselt_b
      nusselt = max(nusselt_a, nusselt_b, nusselt)
  return pi * nusselt * lf * (tcond - tar)

def CIGRE_PConvNatural(ra):
  if (ra > 100) & (ra < 1e4):
    return 0.85 * ra**0.188
  elif ra < 1e6:
    return 0.48 * ra**0.25
  else:
    raise Exception(f'Número de Rayleigh fora do alcance de validade ({ra}) ')

def CIGRE_PConvForcada(re, ataque, rugcond):
  if (re > 100) & (re < 2650):
    b1 = 0.641
    n = 0.471
  elif re < 5e4:
    if rugcond < 0.05:
      b1 = 0.178
      n = 0.633
    else:
      b1 = 0.048
      n = 0.8
  nusselt = b1 * re**n  
  a1 = 0.42
  if ataque < 24*pi/180:
    b2 = 0.68
    m1 = 1.08
  else:
    b2 = 0.58
    m1 = 0.9
  return nusselt * (a1 + b2 * sin(ataque) **m1)

def tempCondutorCigre(amp: float, velVento: float, ataque: float, tempAr: float, radglobal: float, alt: float, cabo: dbCabo, rugcond=0.9, absorcao=0.93, emicond=0.95) -> float:
  """Cálculo da temperatura do condutor dada a corrente

  amp -- corrente em regime permanente (A)
  velVento -- velocidade do vento (m/s)
  ataque -- ângulo de ataque do vento (rad) (pi/2 = perpendicular ao cabo)
  tar -- temperatura do ar (°C)
  radglobal -- radiação solar (W/m²)
  alt -- altura do condutor (m)
  cabo -- Objeto cabo conforme base de dados de exemplo
  rugcond -- rugosidade do condutor
  absorcao -- coeficiente de absorcao solar (0.3 para cabos brilhantes, 0.93 para cabos envelhecidos/poluidos)
  emicond -- taxa de emissividade (0.5 para oxidados, 0.95 envelhecidos, 0.96 molhados)

  Returns:
  temp -- temperatura de operação (°C)
  """
  if (np.isnan([velVento, tempAr, radglobal]).any()):
    return np.nan
  t0 = tempAr
  t1 = tempAr + 150.
  root = ridder(ampacidadeCigreMin, t0, t1, args=(amp, velVento, ataque, tempAr, radglobal, alt, cabo, rugcond, absorcao, emicond))
  
  return root

def parametrosGumbel(n: int) -> tuple[float, float]:
  """
  Cálculo dos parâmetros de Gumbel
  
  Parameters
  ----------

  n : int
    Período de observação

  Returns:
  c1
  c2
  """
  c1 = 0.
  c2 = 0.
  zi = [0.0] * n
  for i in range(n):
    zi[i] = -log(-log((i + 1) / (n + 1)))
  for a in zi:
    c2 += a
  c2 = c2 / n
  for a in zi:
    c1 += (a - c2)**2
  c1 = sqrt(c1 / n)

  return c1, c2

def calcVelVento(vel: float, anos: int, tret: float, cv: float) -> float:
  """Cálculo da velocidade do vento para um tempo de registro, média e desvio padrão (coeficiente de variação)
  Baseado na distribuição de Gumbel

  vel -- Média das velocidades máximas anuais da série de dados
  anos -- Tempo de registro (anos)
  tret -- Tempo de retorno (anos)
  cv -- Coeficiente de variação da série de dados (pu)

  Returns:
  v -- Velocidade do vento para o tempo de retorno
  """
  (c1, c2) = parametrosGumbel(anos)
  ktn = (-log(-log(1 - 1. / tret)) - c2) / c1
    
  return vel * (1. + ktn * cv)



