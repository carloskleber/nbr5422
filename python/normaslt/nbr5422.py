#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, exp, log, sqrt
import numpy as np
from scipy.stats import norm
from warnings import warn
from normaslt import types
"""
Biblioteca de funções da NBR 5422 - revisão 2023
"""

def anguloBalanco(v:float, q0:float, d:float, pcond: float, Vv:float, Vp:float) -> float:
  """
  Ângulo de balanço
  Seção 
  """
  if v < 10:
    k = 1.0
  else:
    k = 3.68 * exp(-0.163*v) + 0.3
  return atan2(k *q0 * d * Vv, pcond * Vp)

def dra(p:float, t:float) -> float:
  """
  Densidade relativa do ar
  Seção 
  """
  t0 = 20
  p0 = 1013
  return p/p0 * (273+t0)/(273+t)

def espacFFFrenteLenta(Us:float, Kcs:float, Fsfl:float, kg:float, kafl:float, zfl=0.06, alpha=0.33) -> float:
  """
  Espaçamento fase-fase para sobretensões de frente lenta
  Seção 9.4.2.4
  Calcula-se primeiro por Kishizima (https://doi.org/10.1109/TPAS.1984.318451),
  caso a distância fique acima a 4 m, recalcula-se pela fórmula do EPRI
  (AC Transmission Line Reference Book 200 kV and Above, 3rd ed., 2005).
  Caso d > 10 m, um warning é lançado.
  Us = Tensão entre fases eficaz da linha em kV
  Kcs = Fator de coordenação estatístico (Anexo C)
  Fsfl = Fator de sobretensão de frente lenta
  kafl = Fator de correção atmosférico
  kg = Fator de gap fase-terra, Anexo C
  zfl = Variação de distribuição de probabilidade
  alpha = Relação entre sobretensões de polaridade positiva e negativa: alpha = un/ (up + un)
  """
  kzfl = 1 - 1.3*zfl
  d = 2.17 * exp(Kcs * sqrt(2) * Us * Fsfl / (1080 * kafl * kzfl * kg) - 1)
  if (d > 4):
    u50 = 1.4 * Kcs * sqrt(2) * Us * Fsfl / (kafl * kzfl)
    r = 54.3115*alpha**2 + 212.6589*alpha - 0.1019*u50 + 286.0043
    if (r < 0):
      # raise('Erro de limite de validade do modelo (raiz de número negativo).')    
      return float("NaN")
    d = 15.3726 + 7.0846 * alpha - sqrt(r)
  if (d > 10):
    warn('Distância calculada fora da validade do modelo: %d m.' % d)
  return d

def espacFFFreqFund(Us:float, Ftmo:float, kaff:float, kgff:float, zff=0.03) -> float:
  """
  Espacamento fase-fase em frequencia fundamental
  Seção 9.3.2.1
  Us = Tensão entre fases norminal eficaz em kV
  Ftmo = Fator da tensão máxima de operação em pu
  kaff = 
  kgff = 
  zff = (default 0.03)
  """
  kzff = 1. - 3. * zff
  return 1.64 * (exp(Us* Ftmo / (750 * kaff * kzff * kgff)) - 1) ** 0.833

def espacFTFrenteLenta(Us:float, Kcs:float, Fsfl:float, kafl:float, kg:float, zfl=0.06) -> float:
  """
  Espaçamento fase-terra para sobretensões de frente lenta
  Seção 9.4.1.1
  """
  kzfl = 0.922 * (1-1.3 * zfl)
  return 2.17 * exp(Kcs*sqrt(2)*Us*Fsfl / (1080 * sqrt(3) * kafl * kzfl * kg) - 1)

def espacFTFreqFund(Us:float, Ftmo:float, kaff:float, kgff:float, zff=0.03) -> float:
  """
  Espaçamento fase-terra para frequência fundamental
  Seção 9.3.1.1
  """
  kzff = 1. - 3. * zff
  return 1.64 * (exp(Us * Ftmo / (750 * sqrt(3) * kaff * kzff * kgff)) - 1)**0.833

def fatorAtmFrenteLenta(dra:float, h:float, d:float) -> float:
  """
  Fator de correção atmosférico para impulsos de frente lenta, linhas CA
  dra - densidade relativa do ar
  h - umidade absoluta do ar em g/m3
  d - espaçamento no ar em m
  """
  hc = 1 + 0.012 * (h / dra - 11.)
  if (d <= 3.5):
    g0 = 1080. / (500. * d) * log(0.46 * d + 1)
  else:
    g0 = 3400. / (500. * d + 4000.)
  m2 = 1.25 * g0 * (g0 - 0.2)
  return dra**m2 * hc**m2

def fatCorrAlt(rug: types.rug, alt: float) -> float:
  """
  Fator de correção da altura
  Seção 4.9.4.4. - Tabela 3
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

def fatorKgFFFrenteLenta(gap: types.gap, alpha=0.33) -> float:
  """
  Fator Kg fase-fase

  """
  if (alpha == 0.5):
    match gap:
      case types.gap.ANEL_ANEL:
        return 1.8
      case types.gap.CONDUTOR_CRUZADO:
        return 1.65
      case types.gap.CONDUTOR_PARALELO:
        return 1.62
      case types.gap.BARRAMENTO:
        return 1.50
      case types.gap.ASSIMETRICO:
        return 1.45
      case _:
        raise ValueError('Tipo invalido')
  elif (alpha == 0.33):
    match gap:
      case types.gap.ANEL_ANEL:
        return 1.7
      case types.gap.CONDUTOR_CRUZADO:
        return 1.53
      case types.gap.CONDUTOR_PARALELO:
        return 1.52
      case types.gap.BARRAMENTO:
        return 1.40
      case types.gap.ASSIMETRICO:
        return 1.36
      case _:
        raise ValueError('Tipo invalido')
    end
  else:
    raise ValueError('Fator alpha nao previsto')


def fatorKgFTFrenteLenta(gap: types.gap) -> float:
  """
  Fator Kg fase-terra
  Tabela C.1 (baseada na NBR 8186:2021)
  """
  match gap:
    case types.gap.CONDUTOR_BRACO:
      return 1.45 # Entre 1.36 a 1.58
    case types.gap.CONDUTOR_JANELA:
      return 1.25 # Entre 1.22 a 1.32
    case types.gap.CONDUTOR_PLANO_ABAIXO:
      return 1.15 # Entre 1.18 a 1.35
    case types.gap.CONDUTOR_HASTE_ABAIXO:
      return 1.47 # ?
    case types.gap.CONDUTOR_ESTRUTURA_LATERAL:
      return 1.45 # Entre 1.28 a 1.63
    case types.gap.ESTRUTURA_HASTE: # e.g. seccionadora aberta
      return 1.35 # Entre 1.03 a 1.66
    case _:
      raise ValueError('Tipo invalido')
  end 

def fatorVentoVao(L: float) -> float:
  """
  Fator de efetividade para correção do comprimento do vão
  Seção 8.5.2.2, Figura 17  
  """
  if L < 200:
    return 1.0
  elif L > 800:
    return 0.858
  else:
    return 1.693e-10*L**3 - 1.093e-7*L**2 - 0.0002686*L + 1.057

def massaAr(alt:float, t:float) -> float:
  """
  Massa específica do ar para cálculo da pressão dinâmica do vento
  Seção 4.7
  """
  return 1.225 * 288.15 / (t + 273.15) * exp(-1.2e-4 * alt)

def risco(Kcs:float, Ngaps:int, sigma:float, sigma_S:float) -> float:
    """
    Cálculo do risco
    Figuras C.1
    Baseado na rotina risco_Kcs.py 
    Kcs = coeficiente estatístico = U90/V2
    Ngaps = número de gaps em paralelo
    sigma = desvio-padrão das sobretensões
    sigma_S = desvio-padrão da suportabilidade
    """

    #SOBRETENSÕES:
    V50 = 1                   #valor médio (pu)
    V2  = V50*(1+2.05*sigma_S)  #máxima estatística 2% (pu)
    
    #SUPORTABILIDADE:
    U90 = Kcs*V2            #tensão com 90% de probabilidade de descarga (pu)
    U50 = U90/(1-1.28*sigma)  #tensão com 50% de probabilidade de descarga (pu)
    
    #VETORES:
    umin = V50*(1-5*sigma_S)
    umax = U50*(1+5*sigma)
    du = 0.001
    u = np.arange(umin, umax, du)
    sob = norm.pdf(u,V50,V50*sigma_S)
    sup = norm.cdf(u,U50,U50*sigma)    
    ris = sob*(1-(1-sup)**Ngaps)
    return(sum(ris))

def umidAbs(dra:float, t:float) -> float:
  """
  Umidade absoluta do ar
  Seção 4.6.1
  Usando DRA (em pu), ao contrário da fórmula que pede em porcentagem.
  """
  return (611. * dra * exp(17.6 * t/(243 + t))) / (0.4615 * (273 + t))

