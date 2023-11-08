import sys

sys.path.insert(0, "C:/Users/jbekkali/WORK/personal/github_actions/GH_A_test")

from src.code_1 import reduced_price

def test_reduced_price():
    assert reduced_price(100, 0.50) == 50
    assert reduced_price(80, 0.50) == 40
    assert reduced_price(50, 0.50) == 25
    assert reduced_price(10, 0.50) == 5
