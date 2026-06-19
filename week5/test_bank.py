from fuel import convert, gauge
import pytest

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_ZeorDividionError():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_negative_fraction():
    with pytest.raises(ValueError):
        convert("-1/2")
def test_ValueError():
    with pytest.raises(ValueError):
        convert("cat/manjeet")


