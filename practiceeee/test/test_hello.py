# we can also check a folder of tests with the help of pytest

from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_argument():
    assert hello('Fizaan') == 'Hello, Fizaan'

# we have to make __init__.py to tell python that treat that folder as packageee
