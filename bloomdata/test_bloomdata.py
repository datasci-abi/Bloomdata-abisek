# pylint: disable=import-error

"""Import functions"""
import pytest
import bloomdata.bloomdata as bd


def test_increment_int():
    """Testing test_increment"""
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1

def test_increment_float():
    """Testing test_increment_folat"""
    assert bd.increment(1.5) == 2.5

def test_increment_int_return_type():
    """Testing test_increment_int_return_type"""
    assert isinstance(bd.increment(3), int)
