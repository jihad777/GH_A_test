import sys
import pytest

sys.path.insert(0, "C:/Users/jbekkali/WORK/personal/github_actions/GH_A_test")

from src.code_1 import reduced_price

print(reduced_price(100, 0.50))

# A comment

def test_reduced_price():
    assert reduced_price(100, 0.50) == 50

print("This is feature 1 update")