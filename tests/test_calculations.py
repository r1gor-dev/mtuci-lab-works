import pytest

from calculations import analyze_data, calculation_average, count_positive, find_max


def test_analyze_data_positive():
    assert analyze_data([1, 2, 3, 4, 5]) == (1, 5, 3.0)


def test_analyze_data_negative():
    assert analyze_data([-10, -5, -20]) == (-20, -5, -11.666666666666666)


def test_analyze_data_mixed():
    assert analyze_data([-10, 0, 10]) == (-10, 10, 0.0)


def test_analyze_data_single_num():
    assert analyze_data([52]) == (52, 52, 52.0)


def test_analyze_data_empty():
    with pytest.raises(ValueError):
        analyze_data([])


def test_average_empty_list():
    with pytest.raises(ValueError):
        calculation_average([])


def test_calculaction_average():
    assert calculation_average([10, 20, 30]) == 20
    assert calculation_average([0, 0, 0]) == 0


def test_find_max():
    assert find_max([-10, -5, -20]) == -5
    assert find_max([1, 5, 3, 9, 2]) == 9


def test_count_positive():
    assert count_positive([-1, 0, 1]) == 1
    assert count_positive([-5, -10]) == 0
