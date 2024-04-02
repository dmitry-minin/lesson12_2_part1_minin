from utils import arrs, dicts


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 1, 3) == []
    assert arrs.my_slice([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_get_val():
    assert dicts.get_val({'a': 1, 'b': 2}, 'a') == 1
    assert dicts.get_val({'a': 1, 'b': 2}, 'c', 'test') == 'test'
    assert dicts.get_val({'a': 1, 'b': 2}, 'a', 'test') == 1
    assert dicts.get_val({}, 'c', 'test') == 'test'



