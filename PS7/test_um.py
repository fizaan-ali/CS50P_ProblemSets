from um import count

def test_middle():
    assert count('yummy') == 0
    assert count('bumm') == 0

def test_upper():
    assert count('Um...') == 1
    assert count('UM') == 1

def test_line():
    assert count('Hello there, um, how are you? um...') == 2
    assert count('My name is, um, Fizaan') == 1
