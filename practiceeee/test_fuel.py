from fuel import convert, gauge
import pytest

def test_convert_negative():
    with pytest.raises(ValueError):
        convert('-1/-1')
    with pytest.raises(ValueError):
        convert('-1/3')
    with pytest.raises(ValueError):
        convert('3/-4')

def test_convert_greater():
    with pytest.raises(ValueError):
        convert('5/4')

def test_convert_yzero():
    with pytest.raises(ZeroDivisionError):
        convert('3/0')

def test_convert_values():
    assert convert('1/4') == 25
    assert convert('1/3') == 33
    assert convert('2/3') == 67
    assert convert('1/1') == 100
    assert convert('0/1') == 0

def test_gauge():
    assert gauge(0) == 'E'
    assert gauge(99) == 'F'
    assert gauge(67) == '67%'
