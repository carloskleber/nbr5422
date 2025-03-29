#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, exp, log, sqrt, radians
import numpy as np
from scipy.stats import norm
from warnings import warn
from normaslt import types
"""
Biblioteca de funções da NBR 5422:2024
"""

def anguloBalanco(v: float, q0: float, d: float, pcond: float, Lm=1., Lp=1., VpVv=-1.) -> float:
  """Ângulo de balanço
  Seção 8.9.1

  Args:
  v -- velocidade do vento em m/s referida a 30 s
  q0 -- pressão dinâmica em Pa
  d -- diâmetro do cabo em m
  pcond -- peso linear do cabo em N/m
  Lm -- vão médio (ou de vento) em m
  Lp -- vão gravante (ou de peso) em m
  VpVv -- relação vão de peso por vão de vento
  """
  if VpVv == -1:
    VpVv = Lp/Lm

  if v < 10:
    k = 1.0
  else:
    k = 3.68 * exp(-0.163*v) + 0.3
  return atan2(k * q0 * d, pcond * VpVv)

def anguloBalancoAssincrono(v: float, beta: float) -> tuple[float, float]:
  """Ângulo de balanço assíncrono
  Seção 8.9.3
  Retorna a variação mínima e máxima do ângulo de balanço
  
  Args:
  v -- vento de projeto em m/s
  beta -- ângulo de balanço médio em rad

  Returns:
  bmin -- ângulo mínimo em rad
  bmax -- ângulo máximo em rad
  """
  sigma = 2.25 * (1 - exp(-v**2/230.))
  bmax = beta + 2 * radians(sigma)
  bmin = beta - 2 * radians(sigma)

  return bmin, bmax

def dra(p:float, t:float) -> float:
  """
  Densidade relativa do ar
  Seção 
  """
  t0 = 20
  p0 = 1013
  return p/p0 * (273+t0)/(273+t)

def espacFFFrenteLenta(Us:float, Kcs:float, Fsfl:float, kg:float, kafl:float, zfl=0.06, alpha=0.33) -> float:
  """Espaçamento fase-fase para sobretensões de frente lenta
  Seção 9.4.2.4
  Calcula-se primeiro por Kishizima (https://doi.org/10.1109/TPAS.1984.318451),
  caso a distância fique acima a 4 m, recalcula-se pela fórmula do EPRI
  (AC Transmission Line Reference Book 200 kV and Above, 3rd ed., 2005).
  Caso d > 10 m, um warning é lançado.
  
  Args:
  Us -- Tensão entre fases eficaz da linha em kV
  Kcs -- Fator de coordenação estatístico (Anexo C)
  Fsfl -- Fator de sobretensão de frente lenta
  kafl -- Fator de correção atmosférico
  kg -- Fator de gap entre fases, Anexo C
  zfl -- Variação de distribuição de probabilidade
  alpha -- Relação entre sobretensões de polaridade positiva e negativa: alpha = un/ (up + un)
  """
  kzfl = 1 - 1.3*zfl
  d = 2.17 * exp(Kcs * sqrt(2) * Us * Fsfl / (1080 * kafl * kzfl * kg* sqrt(3)) - 1)
  if (d > 4):
    u50 = 1.4 * Kcs * sqrt(2) * Us * Fsfl / (kafl * kzfl * sqrt(3))
    r = 54.3115*alpha**2 + 212.6589*alpha - 0.1019*u50 + 286.0043
    if (r < 0):
      # raise('Erro de limite de validade do modelo (raiz de número negativo).')    
      return float("NaN")
    d = 15.3726 + 7.0846 * alpha - sqrt(r)
  if (d > 10):
    warn('Distância calculada fora da validade do modelo: %d m.' % d)
  return d

def espacFFFreqFund(Us:float, Ftmo:float, kaff:float, kgff=-1., zff=0.03, kg=-1.) -> float:
  """Espacamento fase-fase em frequência fundamental
  Seção 9.3.2.1

  Args:
  Us -- Tensão entre fases norminal eficaz em kV
  Ftmo -- Fator da tensão máxima de operação em pu
  kaff -- 
  kgff -- Fator de gap entre fases
  zff -- (default 0.03)
  """
  if kg != -1.:
    kgff = 1.35*kg -0.35*kg**2

  if kgff == -1.:
    raise("Necessário definir kg ou kgff.")

  kzff = 1. - 3. * zff
  return 1.64 * (exp(Us* Ftmo / (750 * kaff * kzff * kgff)) - 1) ** 0.833

def espacFFFrenteRapida(ufr:float, kafr:float, kg=-1., zfr=0.03, kgfr=-1.) -> float:
  """Espaçamento fase-fase para sobretensões de frente rápida
  Seção 9.5.2
  """
  if kg != -1.:
    kgfr = 0.74 + 0.26 * kg

  if kgfr == -1.:
    raise("Necessário definir kg ou kgfr.")
  
  kzfr = 1. - 1.3 * zfr
  return 1.2 * ufr / (530. * kafr * kzfr * kgfr)

def espacFTFrenteLenta(Us:float, Kcs:float, Fsfl:float, kafl:float, kg:float, zfl=0.06) -> float:
  """Espaçamento fase-terra para sobretensões de frente lenta
  Seção 9.4.1.1
  """
  kzfl = 0.922 * (1-1.3 * zfl)
  return 2.17 * exp(Kcs*sqrt(2)*Us*Fsfl / (1080 * sqrt(3) * kafl * kzfl * kg) - 1)

def espacFTFreqFund(Us:float, Ftmo:float, kaff:float, kgff=-1., zff=0.03, kg=-1.) -> float:
  """Espaçamento fase-terra para frequência fundamental
  Seção 9.3.1.1
  """
  if kg != -1.:
    kgff = 1.35*kg - 0.35*kg**2

  if kgff == -1.:
    raise("Necessário definir kg ou kgff.")
  
  kzff = 1. - 3. * zff
  return 1.64 * (exp(Us * Ftmo / (750 * sqrt(3) * kaff * kzff * kgff)) - 1)**0.833

def espacFTFrenteRapida(ufr:float, kafr:float, kg=-1., zfr=0.03, kgfr=-1.) -> float:
  """Espaçamento fase-terra para sobretensões de frente rápida
  Seção 9.5
  """
  if kg != -1.:
    kgfr = 0.74 + 0.26 * kg

  if kgfr == -1.:
    raise("Necessário definir kg ou kgfr.")
  
  kzfr = 1. - 1.3 * zfr
  return ufr / (530. * kafr * kzfr * kgfr)

def fatAtmFrenteLenta(dra:float, h:float, d:float) -> float:
  """Fator de correção atmosférico para impulsos de frente lenta, linhas CA

  Args:
  dra -- densidade relativa do ar
  h -- umidade absoluta do ar em g/m³
  d -- espaçamento no ar em m
  """
  hc = 1 + 0.012 * (h / dra - 11.)
  if d <= 3.5:
    g0 = 1080. / (500. * d) * log(0.46 * d + 1)
  else:
    g0 = 3400. / (500. * d + 4000.)
  m2 = 1.25 * g0 * (g0 - 0.2)
  return dra**m2 * hc**m2

def fatCorrRug(rug=types.rug.B) -> float:
  """Fator de correção da rugosidade do terreno
  Seção 4.9.4.2. - Tabela 1
  """
  match rug:
    case types.rug.A:
      return 1.08
    case types.rug.B:
      return 1.
    case types.rug.C:
      return 0.85
    case types.rug.D:
      return 0.67
    case _:
      warn("Classe de rugosidade inválida.")

def fatCorrInt3s(rug=types.rug.B) -> float:
  """Fator de correção do período de integração 3 s
  Seção 4.9.4.3. - Tabela 2
  """
  match rug:
    case types.rug.A:
      return 1.31
    case types.rug.B:
      return 1.41
    case types.rug.C:
      return 1.58
    case types.rug.D:
      return 1.88
    case _:
      warn("Classe de rugosidade inválida.")

def fatCorrInt30s(rug=types.rug.B) -> float:
  """Fator de correção do período de integração 30 s
  Seção 8.2.2.1. - Tabela 9
  """
  match rug:
    case types.rug.A:
      return 1.17
    case types.rug.B:
      return 1.22
    case types.rug.C:
      return 1.30
    case types.rug.D:
      return 1.48
    case _:
      warn("Classe de rugosidade inválida.")

def fatCorrAlt(alt: float, rug=types.rug.B) -> float:
  """Fator de correção da altura
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

def fatEfetividadeVento(v: float) -> float:
  """Fator de vento para correção do do ângulo de balanço com a velocidade do vento
  Figura 22
  """
  if v < 10.:
    return 1.0
  else:
    return 3.68 * exp(-0.163*v) + 0.3

def fatKgFFFrenteLenta(gap: types.gap, alpha=0.33) -> float:
  """Fator Kg fase-fase
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
  else:
    raise ValueError('Fator alpha nao previsto')


def fatKgFTFrenteLenta(gap: types.gap) -> float:
  """Fator Kg fase-terra
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

def fatTurb(regiao: types.regiao) -> float:
  """Fator de turbulencia
  Tabela 3
  """
  match regiao:
    case types.regiao.S:
      return 1.08
    case types.regiao.SE | types.regiao.CO:
      return 1.12
    case types.regiao.N | types.regiao.NE:
      return 1.16
    case _:
      raise ValueError('Regiao invalida')

def distSegurancaVert(obstaculo: types.obs, regime: types.amp, hobs: float, Us:float, Fsfl:float, kafl:float, zfl=0.06) -> float:
  """Distância vertical de segurança
  Tabela 5

  Args:
  obstaculo -- Tipo de obstáculo
  regime -- Regime e condição operativa, conforme Seção 5.4/ Tabela 4.
  hobs -- Altura do obstáculo, dependendo do tipo, será assumido o valor mínimo por norma
  Us -- Tensão nominal em kV
  Fsfl --  
  kafl --  
  """
  match obstaculo:
    case types.obs.PEDESTRE:
      kg = 1.47
      hmin = 3.90
      dPbv = 0.30
    case types.obs.MAQ_AGRICOLA:
      kg = 1.18
      hmin = 4.00
      dPbv = 0.40
    case types.obs.RODOVIA:
      kg = 1.18
      hmin = 5.40
      dPbv = 0.50
    case types.obs.FERROVIA_NAO_ELETRIFICADA:
      kg = 1.18
      hmin = 6.40
      dPbv = 0.50
    case types.obs.FERROVIA_ELETRIFICADA:
      kg = 1.40
      hmin = 9.70
      dPbv = 0.50
    case types.obs.SUPORTE_FERROVIA:
      kg = 1.18
      hmin = 0.
      dPbv = 1.90
    case types.obs.AGUAS_NAVEGAVEIS:
      kg = 1.47
      hmin = 0.
      dPbv = 4.20
    case types.obs.AGUAS_NAO_NAVEGAVEIS:
      kg = 1.47
      hmin = 3.60
      dPbv = 0.60
    case types.obs.LINHA_TRANSMISSAO:
      kg = 1.45
      hmin = 0.
      dPbv = 0.80
    case types.obs.LINHA_TELECOM:
      kg = 1.45
      hmin = 0.
      dPbv = 0.80
    case types.obs.VEGETACAO_PERM:
      kg = 1.18
      hmin = 0.
      dPbv = 2.10
    case types.obs.CULT_AGRIC_PERM:
      kg = 1.18
      hmin = 0.
      dPbv = 2.10
    case types.obs.INSTALACAO_TRANSP:
      kg = 1.18
      hmin = 0.
      dPbv = 1.00
    case _:
      raise ValueError('Tipo de obstáculo inválido')

  hobs = max(hmin, hobs)
  Pbv = hobs + dPbv
  
  # Petipn e Petips são iguais
  Petip = espacFTFrenteLenta(Us, 1.35, Fsfl, kafl, kg, zfl)
  Pelim = espacFTFrenteLenta(Us, 1.25, Fsfl, kafl, kg, zfl)
  match regime:
    case types.amp.TIPICA_NOMINAL:
      dv = max(Pbv + 0.90 + Petip, Pbv + 0.60 + Pelim + 0.90)
    case types.amp.TIPICA_SOBRECORRENTE:
      dv = Pbv + 0.60 + Petip
    case types.amp.LIMITE_NOMINAL:
      dv = Pbv + 0.60 + Pelim
    case types.amp.LIMITE_SOBRECORRENTE:
      dv = Pbv + Pelim
    case _:
      raise ValueError('Regime inválido')
    
  return dv
      
def fatCombVentoCabo(rug: types.rug, h: float) -> float:
  """Fator combinado de vento aplicado a cabos
  Seção 8.5.2.3, Figura 16, Tabela 10
  """
  if h < 10:
    h = 10.

  match rug:
    case types.rug.A:
      return 0.2914*log(h) + 1.0468
    case types.rug.B:
      return 0.3733*log(h) + 0.9762
    case types.rug.C:
      return 0.4936*log(h) + 0.9214
    case types.rug.D:
      return 0.6153*log(h) + 0.8144
    case _:
      raise ValueError('Classe de rugosidade invalida')

def fatCombVentoSuportes(rug: types.rug, h: float) -> float:
  """Fator combinado de vento aplicado a suportes e cadeia de isoladores
  Seção 8.6.3, Figura 18, Tabela 11
  """
  if h < 10:
    h = 10.

  match rug:
    case types.rug.A:
      return -0.0002 * h**2 + 0.0232 * h + 1.4661
    case types.rug.B:
      return -0.0002 * h**2 + 0.0274 * h + 1.6820
    case types.rug.C:
      return -0.0002 * h**2 + 0.0298 * h + 2.2744
    case types.rug.D:
      return -0.0002 * h**2 + 0.0384 * h + 2.9284
    case _:
      raise ValueError('Classe de rugosidade invalida')

def fatVentoVao(L: float) -> float:
  """Fator de efetividade para correção do comprimento do vão
  Seção 8.5.2.2, Figura 17  
  """
  if L < 200:
    return 1.0
  elif L > 800:
    return 0.858
  else:
    return 1.693e-10*L**3 - 1.093e-7*L**2 - 0.0002686*L + 1.057

def coefArrastoCabos(d: float) -> float:
  """Coeficiente de arrasto do cabo
  Seção 8.5.2.1
  """
  if d <= 0.015:
    return 1.0
  else:
    return 1.2

def coefArrastoElemCilindrico(Vp: float, d: float) -> float:
  """Coeficiente de arrasto em suportes, elementos cilíndricos de grande diâmetro
  Seção 8.8.3.2, Figura 21
  """
  Re = d * Vp/ 1.45e-5
  if Re < 3e5:
    Cxtc = 1.2
  elif Re > 4.5e5:
    Cxtc = 0.75
  else:
    Cxtc = -1.1098 * log(Re) + 15.197
  return Cxtc

def massaAr(alt:float, t:float) -> float:
  """Massa específica do ar para cálculo da pressão dinâmica do vento
  Seção 4.7
  """
  return 1.225 * 288.15 / (t + 273.15) * exp(-1.2e-4 * alt)

def risco(Kcs:float, Ngaps:int, sigma:float, sigma_S:float) -> float:
  """Cálculo do risco
  Figuras C.1
  Baseado na rotina risco_Kcs.py 

  Args:
  Kcs -- coeficiente estatístico = U90/V2
  Ngaps -- número de gaps em paralelo
  sigma -- desvio-padrão das sobretensões
  sigma_S -- desvio-padrão da suportabilidade
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
  """Umidade absoluta do ar
  Seção 4.6.1
  Usando DRA em pu, ao contrário da fórmula que pede em porcentagem.

  Args:
  dra --
  t -- 
  """
  return (611. * dra * exp(17.6 * t/(243 + t))) / (0.4615 * (273 + t))

