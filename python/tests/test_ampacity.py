import pytest
from normaslt import geral

@pytest.fixture
def condutor1():
  return geral.dbCabo.CAL_SELENIUM

def test_ampacidade(condutor1):
