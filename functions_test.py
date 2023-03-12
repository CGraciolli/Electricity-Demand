import pytest
from functions import getList, getFFT, jsonFFT, jsonWelch

def test_getList():
    list1 = []
    list2 = [{"a" : "2"}]
    list3 = [{"a": 2, "b": 5}, {"a": 4, "b": 7}]

    assert getList(list1, "value") == []
    assert getList(list2, "a") == ["2"]
    assert getList(list3, "b") == [5, 7]

def test_getFFT():
    