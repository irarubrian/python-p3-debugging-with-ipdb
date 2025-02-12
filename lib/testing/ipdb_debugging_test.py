import pytest
from ipdb_debugging import *  # Ensure this module exists and contains `plus_two`

class TestIpdbDebugging:
    '''Tests for ipdb_debugging.py'''
    
    def test_adds_two(self):
        '''plus_two() adds 2 to input arg and returns sum.'''
        assert plus_two(3) == 5  # No need to return test

# Define plus_two function (if it's missing from `ipdb_debugging.py`)
def plus_two(num):
    return num + 2

# Use pytest to parametrize multiple test cases
@pytest.mark.parametrize("num2, expected", [(2, 4), (3, 5), (10, 12)])
def test_plus_two(num2, expected):
    assert plus_two(num2) == expected
