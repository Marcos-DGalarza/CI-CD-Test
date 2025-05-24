def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0.3, 0.7) == 1

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9, 3) == 3
    
def test_resta():
    assert resta(5, 2) == 3
    assert resta(1, 1) == 0


#comentario luciano





