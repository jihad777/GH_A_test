import pytest
import sys

sys.path.insert(0, "/home/runner/work/GH_A_test/GH_A_test/tests")

from code_1 import reduced_price

def Test_reduced_price():
    assert reduced_price(100, 0.50) == 50