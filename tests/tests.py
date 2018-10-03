import pytest
from .models import Calculadora
from business import ParametroNegativoException
from business import ResultadoNegativoException
from business import ParametroZeroException
from business import OperacaoMuitoFacilException

def test_soma():
    try:
        assert Calculadora().soma(1, 1) == 2
    except ParametroNegativoException:
        print ('Apenas numeros positivos devem ser utilizados como parametro')

def test_subtracao():
    try:    
        assert Calculadora().subtrai(1, 1) == 0
        if resultado < 0:
            except ResultadoNegativoException:

    except ParametroNegativoException:
        print ('Apenas numeros positivos devem ser utilizados como parametro')

def test_multiplicacao():
    try:
        assert Calculadora().multiplica(10, 2) == 20

def test_divisao():
    with pytest.raises(ZeroDivisionError):
    try:
        Calculadora().divide(10,0)



    
        