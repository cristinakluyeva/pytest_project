import pytest
from utils import arrs

@pytest.mark.parametrize('array, index_array_part, default, result', [
    ([3, 6, 8, 9, 0], 3, "lose", 9),
    (["ok", "good", "not_bad"], 1, "lose", "good"),
    ([3, 6, 8, 9, 0], 3, "lose", 9),
    ([3, 6, 8, 9, 0], -2, "lose", "lose"),
    ([0.9, 0.5, "hello"], -2, "lose", "lose")
])


def test_pytest_get(array, index_array_part, default, result):
    assert arrs.get(array, index_array_part, default) == result


def test_get():
    assert arrs.get(["cat", "dog"], 0, "lose") == "lose"


def test_slice():
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([0, 0, 0], -1) == [0]
    assert arrs.my_slice(["a", "b", "c", "d"], -5, -2) == ["a", "b"]
    assert arrs.my_slice(["a", "b", "c", "d"], 0, -2) == ["a", "b"]
