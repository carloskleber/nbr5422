#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import exp, pi, sin, sinh, sqrt
import numpy as np
import pandas as pd
from enum import Enum
from scipy.optimize import ridder
import os.path
from tqdm import tqdm
from urllib.request import urlretrieve
from zipfile import ZipFile 
"""
Biblioteca geral de funções, não associadas a normas
"""
class dbCabo(Enum):
  """Banco de dados de cabos para usar nos exemplos

  Atributos:
  desc -- Denominação do cabo
  d -- diâmetro nominal em m
  S -- seção em m²
  p -- peso linear em N/m
  T -- tração de ruptura em N
  E -- módulo de elasticidade em kgf/m²
  alfa1 -- coeficiente de dilatação térmica em 1/°C
  tCA -- Temperatura de referência para resistência CA em °C
  rCA -- resistência CA para cada tCA em Ω/m
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

  TODO prever alteração no peso final (ex. forca do vento)
  """
  
  if alfa1 == 0:
    raise ValueError('Coeficiente linear (alfa1) igual a zero.')
  deltat = t1 - t0
  if deltat == 0:
    T2 = T0
    f = p * A**2 / (8. * T2)
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
  f = p * A**2 / (8. * T2)
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

def getEstacaoINMET(local: str, ano: int) -> tuple[str, float, float, float]:
  """Transcreve o local para o nome do arquivo INMET, de acordo com o período
  Também retorna latitude e longitude
  Localizações das estações: https://mapas.inmet.gov.br/
  """
  s = ''
  match local:
    case 'Bauru':
      lat = -22.358052
      long = -49.028877
      alt = 636.17
      s = 'INMET_SE_SP_A705_BAURU'
    case 'Belém':
      lat = -1.411228
      long = -48.439512
      alt = 21.17
      s = 'INMET_N_PA_A201_BELEM'
    case 'Bento Gonçalves':
      lat = -29.164581
      long = -51.534202
      alt = 623.27
      s = 'INMET_S_RS_A840_BENTO GONCALVES'
    case 'Brasília':
      lat = -15.78944444
      long = -47.92583332
      alt = 1159.54
      s = 'INMET_CO_DF_A001_BRASILIA'
    case 'Cuiabá':
      lat = -15.559295
      long = -56.062951
      alt = 240
      s = 'INMET_CO_MT_A901_CUIABA'
    case 'Rio de Janeiro':
      lat = -22.98833333
      long = -43.19055555
      alt = 25.59
      if ano > 2018:
        s = 'INMET_SE_RJ_A652_RIO DE JANEIRO - FORTE DE COPACABANA'
      else:
        s = 'INMET_SE_RJ_A652_FORTE DE COPACABANA'
    case 'Juti':
      s = 'INMET_CO_MS_A749_JUTI'
      lat = -22.85722222
      long = -54.60555555
      alt = 375.18
    case 'Dourados':
      s = 'INMET_CO_MS_A721_DOURADOS'
      lat = -22.19388888
      long = -54.91138888
      alt = 463.3
    case 'Ivinhema':
      s = 'INMET_CO_MS_A709_IVINHEMA'
      lat = -22.30055555
      long = -53.82277777
      alt = 377.36
    case 'Manaus':
      s = 'INMET_N_AM_A101_MANAUS'
      lat = -3.10361111
      long = -60.01555555
      alt = 61.25
    case 'Recife':
      s = 'INMET_NE_PE_A301_RECIFE'
      lat = -8.05928
      long = -34.959239
      alt = 11.3
    case 'Rio Brilhante':
      s = 'INMET_CO_MS_A743_RIO BRILHANTE'
      lat = -21.77499999
      long = -54.52805554
      alt = 324.31
    case 'São Paulo':
      s = 'INMET_SE_SP_A701_SAO PAULO - MIRANTE'
      lat = -23.496294
      long = -46.620088
      alt = 785.64
    case 'Teresópolis':
      lat = -22.4486111
      long = -42,98694444
      alt = 981
      if ano > 2018:
        s = 'INMET_SE_RJ_A618_TERESOPOLIS-PARQUE NACIONAL'
      else:
        s = 'INMET_SE_RJ_A618_TERESOPOLIS'
    case _:
      raise ValueError('Localização inválida') 
  if ano < 2020:
    return f'{ano}/{s}', lat, long, alt
  else:
    return s, lat, long, alt

def readEstacao(local: str, anoInic: int, anoFim: int) -> tuple[pd.DataFrame, float, float, float]:
  """Retorna o dataframe de um alcance de anos para uma estação INMET
  """
  dados = pd.DataFrame()

  for ano in range(anoInic, anoFim+1):
    url = f'https://portal.inmet.gov.br/uploads/dadoshistoricos/{ano}.zip'
    arqzip = f'{ano}.zip'
    strlocal, lat, long, alt = getEstacaoINMET(local, ano)
    arq = f'{strlocal}_01-01-{ano}_A_31-12-{ano}.CSV'
    if not(os.path.isfile(arqzip)):
      download_with_progress(url, arqzip)
    with ZipFile(arqzip) as zObject:
      zObject.extract(arq) 
    df = pd.read_csv(arq, sep=';', skiprows=8, encoding='latin1', decimal=',')
    df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    # Acertando datas
    if ano < 2019:
      df = df.rename(columns={
        'DATA (YYYY-MM-DD)': 'Data',
        'HORA (UTC)': 'Hora UTC'
      })
    df['Tempo UTC'] = df['Data'] + df['Hora UTC']
    df.drop(['Data', 'Hora UTC'], axis=1, inplace=True)
    if ano < 2019:
      df['Tempo UTC'] = pd.to_datetime(df['Tempo UTC'], format='%Y-%m-%d%H:%M')
    else:
      df['Tempo UTC'] = pd.to_datetime(df['Tempo UTC'], format='%Y/%m/%d%H%M UTC')

    df = df.rename(columns={
        "PRECIPITAÇÃO TOTAL, HORÁRIO (mm)" : "precTotal", 
        "PRESSAO ATMOSFERICA AO NIVEL DA ESTACAO, HORARIA (mB)": "pMed", 
        "PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)": "pMax",
        "PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)": "pMin",
        "RADIACAO GLOBAL (KJ/m²)": "rad",
        "RADIACAO GLOBAL (Kj/m²)": "rad",
        "TEMPERATURA DO AR - BULBO SECO, HORARIA (°C)": "tMed",
        "TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)": "tMax", 
        "TEMPERATURA MÍNIMA NA HORA ANT. (AUT) (°C)": "tMin",
        "TEMPERATURA DO PONTO DE ORVALHO (°C)": "tOrv",
        "TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)": "tOrvMax",
        "TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)": "tOrvMin",
        "UMIDADE RELATIVA DO AR, HORARIA (%)" : "umid",
        "UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)" : "umidMax",
        "UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)" : "umidMin",
        "VENTO, DIREÇÃO HORARIA (gr) (° (gr))": "dirVento",
        "VENTO, RAJADA MAXIMA (m/s)": "ventoRaj", 
        "VENTO, VELOCIDADE HORARIA (m/s)": "ventoHor"})
    # Considerando NaN da radiação solar igual a zero
    df = df.replace(-9999, None)
    df['rad'] = df['rad'].fillna(0)
    df['rad'] = df['rad'] / 3.6 # convertendo kJ/m²/h por J/s (W/m²) 
    dados = pd.concat([dados, df], ignore_index=True)
  # Testando trocar dados inválidos por None em vez de NaN
  # Trocar só no final porque com None o concat troca os tipos
  dados = dados.infer_objects()
  return dados, lat, long, alt

def download_with_progress(url, filename):
  # Define a callback function to update the progress bar
  def reporthook(block_num, block_size, total_size):
      # Calculate the progress
      progress.update(block_num * block_size - progress.n)

  # Initialize the progress bar
  with tqdm(total=100, unit='%', unit_scale=True, desc=filename) as progress:
      urlretrieve(url, filename, reporthook)

def progresso(block_num, block_size, total_size):
  """Exibe barra de progresso para uso com urlretrieve
  """
  global pbar
  if pbar is None:
    pbar = progressbar.ProgressBar(maxval=total_size)
    pbar.start()  
  downloaded = block_num * block_size
  if downloaded < total_size:
    pbar.update(downloaded)
  else:
    pbar.finish()
    pbar = None

def plot_dimension(ax, start, end, offset=0.2, text_offset=0.1, label=""):
    """
    Desenha uma linha de cota
    
    :param ax: Matplotlib Axes object
    :param start: (x, y) tuple for the start point
    :param end: (x, y) tuple for the end point
    :param offset: Distance of the dimension line from the object
    :param text_offset: Distance of the text from the dimension line
    :param label: Label for the dimension
    """
    x1, y1 = start
    x2, y2 = end

    dx, dy = x2 - x1, y2 - y1
    length = np.hypot(dx, dy)
    angle = np.degrees(np.arctan2(dy, dx))
    if not label:
      label = f'{length:.2f}'
    unit_dx, unit_dy = dx / length, dy / length
    perp_dx, perp_dy = -unit_dy * offset, unit_dx * offset
    dim_start = (x1 + perp_dx, y1 + perp_dy)
    dim_end = (x2 + perp_dx, y2 + perp_dy)
    ax.plot([x1, dim_start[0]], [y1, dim_start[1]], 'k-', lw=0.5)
    ax.plot([x2, dim_end[0]], [y2, dim_end[1]], 'k-', lw=0.5)
    ax.plot([dim_start[0], dim_end[0]], [dim_start[1], dim_end[1]], 'k-', lw=0.5)

    # Draw arrowheads
    arrow_size = 0.05 * length
    ax.arrow(dim_start[0], dim_start[1], unit_dx * arrow_size, unit_dy * arrow_size,
             head_width=0.05, head_length=0.05, fc='k', ec='k')
    ax.arrow(dim_end[0], dim_end[1], -unit_dx * arrow_size, -unit_dy * arrow_size,
             head_width=0.05, head_length=0.05, fc='k', ec='k')

    # Add rotated text at the middle of the dimension line
    text_x, text_y = (dim_start[0] + dim_end[0]) / 2, (dim_start[1] + dim_end[1]) / 2
    text_x += text_offset * np.cos(np.radians(angle))  # Offset text slightly
    text_y += text_offset * np.sin(np.radians(angle))
    
    ax.text(text_x, text_y, label, ha='center', va='bottom', fontsize=10, 
            rotation=angle, rotation_mode="anchor")

def minDistance(A, B, E):
  """
  Determina a distancia minima entre um ponto E e um segmento de reta AB 
  Baseado em https://www.geeksforgeeks.org/minimum-distance-from-a-point-to-the-line-segment-using-vectors/
	"""
  AB = [None, None]
  AB[0] = B[0] - A[0]
  AB[1] = B[1] - A[1]
  BE = [None, None]
  BE[0] = E[0] - B[0]
  BE[1] = E[1] - B[1]
  AE = [None, None]
  AE[0] = E[0] - A[0]
  AE[1] = E[1] - A[1] 
  AB_BE = AB[0] * BE[0] + AB[1] * BE[1]; 
  AB_AE = AB[0] * AE[0] + AB[1] * AE[1]; 

	# Minimum distance from 
	# point E to the line segment 
  reqAns = 0 
  if (AB_BE > 0):
    y = E[1] - B[1] 
    x = E[0] - B[0] 
    reqAns = sqrt(x * x + y * y) 
  elif (AB_AE < 0):
    y = E[1] - A[1] 
    x = E[0] - A[0] 
    reqAns = sqrt(x * x + y * y) 
  else:
    x1 = AB[0] 
    y1 = AB[1] 
    x2 = AE[0] 
    y2 = AE[1] 
    mod = sqrt(x1 * x1 + y1 * y1) 
    reqAns = abs(x1 * y2 - y1 * x2) / mod 	
  return reqAns
