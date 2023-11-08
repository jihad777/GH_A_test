import pytest

def reduced_price(amount, reduction):
    final_price = amount - amount*reduction
    return final_price

@pytest.fixture
def test_reduced_price():
    assert reduced_price(100, 0.50) == 50