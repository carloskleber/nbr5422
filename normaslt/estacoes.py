#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path
from zipfile import ZipFile 
"""
Biblioteca de funções de acesso a base de dados meteorológicos.
"""

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