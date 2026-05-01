import pytest
from app import square_func, cube_func, fifth_power_func

def test_square():
    assert square_func(2) == 4

def test_cube():
    assert cube_func(2) == 8

def test_fifth_power():
    assert fifth_power_func(2) == 32