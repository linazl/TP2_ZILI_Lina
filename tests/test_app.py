import sys
sys.path.insert(0, '.')

from app import addition, soustraction

def test_addition():
    """Test de la fonction addition"""
    assert addition(2, 2) == 4
    assert addition(5, 3) == 8
    assert addition(-1, 1) == 0

def test_soustraction():
    """Test de la fonction soustraction"""
    assert soustraction(5, 3) == 2
    assert soustraction(10, 5) == 5
    assert soustraction(0, 0) == 0