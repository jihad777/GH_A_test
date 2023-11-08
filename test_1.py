from code_1 import reduced_price
import pytest

@pytest.fixture
def Test_reduced_price():
    price = 100
    reduction = 0.50
    assert reduced_price(price, reduction) == 50