from plates import is_valid

def test_length():
    assert is_valid('A') == False
    assert is_valid('ABC1234F') == False
    assert is_valid('ABC') == True

def test_start():
    assert is_valid('ABCD') == True
    assert is_valid('12AB34') == False
    assert is_valid('A1B2C3') == False

def test_punctuation():
    assert is_valid('AB#12') == False
    assert is_valid('AB1234') == True
    assert is_valid('A1b_c3') == False

def test_middle():
    assert is_valid('AB1234') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('AB12Bc') == False
    assert is_valid('ABC012') == False