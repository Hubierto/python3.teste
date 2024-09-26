import pytest
from banco.models.conta import Conta

#testes de cobertura

@pytest.fixture
def conta_valida():
    conta1 = Conta(222,333)
    return conta1


def test_numero_conta_valida(conta_valida):
    assert conta_valida._numero_conta == 222

def test_agencia_valida(conta_valida):
    assert conta_valida._agencia == 333

def test_depositar_valor_positivo(conta_valida):
    conta_valida.depositar(100)       
    assert conta_valida._saldo == 100

def test_saldo_inicial_zero(conta_valida):
    assert conta_valida._saldo == 0 


    
 