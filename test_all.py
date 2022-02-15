import pytest
from solution import task_1, is_prime, task_3


def test_task_1():
    vals = [1, 3, 4]
    assert task_1(vals) == 1


def test_is_prime():
    assert is_prime(3) == True


def test_task_3():
    vals = ['0.1', '0,1', "0  , 1", '1', '5']
    assert task_3(vals) == 3
