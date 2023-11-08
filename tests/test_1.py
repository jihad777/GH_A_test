import pytest
import sys

sys.path.insert(0, "/Users/jbekkali/WORK/personal/github_actions/GH_A_test")

from code_1 import reduced_price

@pytest.fixture
def Test_reduced_price():
    assert reduced_price(100, 0.50) == 50