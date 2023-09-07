import math

#def test_sqrt():
    #num = 25
    #assert math.sqrt(num) == 5

#def testsquare():
    #num = 7
    #assert 7*7 == 40

#def tesequality():
    #assert 10 == 11

import math

#def test_greater():
    #num = 100
    #assert num > 100

#def test_greater_equal():
    #num = 100
    #assert num >= 100

#def test_less():
    #num = 100
    #assert num < 200

import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
