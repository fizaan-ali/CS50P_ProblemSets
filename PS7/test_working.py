from working import convert
import pytest

def test_firstformat():
    assert convert('9:00 AM to 5:30 PM') == '09:00 to 17:30'
    assert convert('2:30 PM to 7:00 AM') == '14:30 to 07:00'

def test_secondformat():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('5 PM to 9 AM') == '17:00 to 09:00'

def test_thirdformat():
    assert convert('7:30 AM to 4 PM') == '07:30 to 16:00'

def test_fourformat():
    assert convert('9 PM to 11:30 AM') == '21:00 to 11:30'

def test_edgecases():
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'

def test_invalid():
    with pytest.raises(ValueError):
        convert('12 AM - 5 PM')

def test_alsoinvalid():
    with pytest.raises(ValueError):
        convert('8:60 PM to 80:23 AM')
