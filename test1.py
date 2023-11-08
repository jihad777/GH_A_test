import pytest

def reduced_price(amount, reduction):
    final_price = amount - amount*reduction
    return final_price

def test_reduced_price():
    assert reduction > 0
    assert reduction <= 1
    assert reduced_price(100, 0.50) == 50