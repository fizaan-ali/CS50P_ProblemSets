from numb3rs import validate

def test_range():
    assert validate('255.255.255.255') == True
    assert validate('127.0.0.1') == True
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False

def test_nondigits():
    assert validate('cat') == False
    assert validate('Fizaan') == False

def test_leadingzeros():
    assert validate('192.168.001.1') == False
    assert validate('192.168.10.1') == True
