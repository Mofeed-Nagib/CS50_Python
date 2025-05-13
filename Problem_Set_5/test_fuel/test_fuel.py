from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("0/2") == 0
    assert convert("3/4") == 75
    assert convert("5/5") == 100
    with pytest.raises(ValueError):
        convert("a/1")
    with pytest.raises(ValueError):
        convert("2/b")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(40) == "40%"
    assert gauge(60) == "60%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"