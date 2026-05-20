from hello import hello

def test_argument():
    assert  hello('Fizaan') == 'Hello, Fizaan'

def test_default():
    assert hello() == 'Hello, world'