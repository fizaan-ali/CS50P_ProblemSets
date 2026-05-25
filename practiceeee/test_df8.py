from df8 import validate_date, convert_to_minutes, minutes_to_words
import pytest

def test_get_date():
    assert validate_date('2008-06-06') == '2008-06-06'
    with pytest.raises(SystemExit): # if invalid date then sys.exit()
        validate_date('June 6, 2008')

def test_convert_to_minutes():
    birth = date(2008, 6, 6)
    expected = (date.today() - birth).days * 24 * 60
    assert convert_to_minutes('2008-06-06') == expected

def test_minutes_to_words():
    assert minutes_to_words(9447840) == 'Nine million, four hundred and forty-seven thousand, eight hundred and forty'