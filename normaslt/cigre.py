#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import atan2, exp, log, sqrt, radians
import numpy as np
from scipy.stats import norm
from warnings import warn
from normaslt import types
"""
Biblioteca de funções CIGRE

Modelos apresentados em brochuras técnicas, usualmente referenciados em normas.
"""
def anguloBalancoTB348(v:float, d:float, ncond:int, pcond:float, piso:float, aiso:float, Lm:float, Lp:float, cxc=1, gl=0) -> float:
  """Fórmula de ângulo de balanço conforme TB 348 (eq. 2.14)

  Argumentos:
  v -- velocidade do vento (m/s)
  d -- diâmetro do cabo (m)
  ncond -- número de subcondutores
  pcond -- peso linear por subcondutor (N/m)
  piso -- peso da cadeia de isoladores (N)
  aiso -- área exposta de cadeia de isoladores (m²)
  Lm -- vão médio (ou de vento) em m
  Lp -- vão gravante (ou de peso) em m
  cxc -- Coeficiente de arrasto do condutor
  """

  # Fator de rajada - Ajuste da Fig. 2.3
  if v < 20:
    gc = -7.556e-5*v**3 + 7.867e-3*v**2 - 2.373e-1*v + 2.58
  else:
    gc = 0.36
  q0 = 0.5 * 1.225 * v**2
  # Coeficiente de efetividade - IEC 60826
  # Válido entre 200 e 800 m
  if gl == 0:
    gl = 4e-10 * Lm**3 -5e-7 * Lm**2 -1e-4 * Lm + 1.0403
  qcond = q0 * cxc * gc * gl * d * ncond * Lm
  qiso = q0 * 1.2 * aiso
  pcond = ncond * pcond * Lp
  return atan2(qcond + 0.5 * qiso, pcond + 0.5 * piso)