import sys
import pytest

sys.path.insert(0, '/Users/jbekkali/WORK/personal/github_actions/GH_A_test')

from code_1 import reduced_price

@pytest.fixture
def Test_reduced_price():
    price = 100
    reduction = 50
    assert reduced_price(price, reduction) == 50