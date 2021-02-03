import math

my_list = [5, 7, 8, 9, 14, 2, 4, 3]


def test_filter():
    assert list(filter(lambda x: x > 4, my_list)) == [5, 7, 8, 9, 14]
    assert list(filter(lambda x: x % 2 == 1, my_list)) == [5, 7, 9, 3]


def test_map():
    assert list(map(lambda x: x * 5 - 2, my_list)) == [23, 33, 38, 43, 68, 8, 18, 13]
    assert list(map(lambda x: x % 2, my_list)) == [1, 1, 0, 1, 0, 0, 0, 1]


def test_sorted():
    assert list(sorted(my_list)) == [2, 3, 4, 5, 7, 8, 9, 14]
    assert list(sorted(my_list, reverse=True)) == [14, 9, 8, 7, 5, 4, 3, 2]


def test_pi():
    assert round(math.pi, 4) == 3.1416
    assert round(math.pi, 2) == 3.14


def test_sqrt():
    assert round(math.sqrt(6), 2) == 2.45
    assert math.sqrt(1024) == 32


def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(32, 2) == 1024


def test_hypot():
    assert math.hypot(2, 3) == math.sqrt(2*2 + 3*3)
    assert int(math.hypot(10, 10)) == 14
