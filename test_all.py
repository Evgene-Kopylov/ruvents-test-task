from datetime import datetime

import pytest
from solution import task_1, is_prime, task_3, task_5, task_6


def test_task_1():
    vals = [1, 3, 4]
    assert task_1(vals) == 1


def test_is_prime():
    assert is_prime(3) == True


def test_task_3():
    vals = ['0.1', '0,1', "0  , 1", '1', '5']
    assert task_3(vals) == 3


def test_task_5():
    vals = ['2022-02-15 12:47:45.053136', '2022-02-16 12:47:45.053136']
    print(datetime.now())
    assert task_5(vals) == 1


def test_task_6():
    # 8 - 01 - 2013
    # vals = ['01-16-2021', '02-15-2022', '02-22-2022', '02-29-2022']
    vals = ['01-16-2021', '02-15-2022', '02-22-2022']
    assert task_6(vals) == 1
