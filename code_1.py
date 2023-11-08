import pytest

def reduced_price(amount, reduction):
    final_price = amount - amount*reduction
    return final_price

@pytest.fixture
def Test_reduced_price():
    assert reduced_price(100, 0.50) == 50
    
""" @pytest.fixture
def Test_reduced_price():
    price = 100
    reduction = 50
    assert reduced_price(price, reduction) == 50 """