import pytest
from normaslt import geral
from math import pi

@pytest.fixture
def condutor1():
  return geral.dbCabo.CAA_ZEBRA

def test_ampacidade(condutor1):
  """
  Exemplo Morgan Cigre WG 22.12
  """

  amp = 600
  vvento = 2
  angvento = pi/4
  tempAr = 40
  radglobal = 980
  alt = 1600
  rugcond = 0.9 # não tem na referência, assumido
  absorcao = 0.5
  emicond = 0.5
  t = geral.tempCondutorCigre(amp, vvento, angvento, tempAr, radglobal, alt, condutor1, rugcond, absorcao, emicond)
  print(t)
