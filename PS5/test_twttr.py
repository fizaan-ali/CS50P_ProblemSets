from twttr import shorten

def test_word():
    assert shorten('Fizaan') == 'Fzn'
    assert shorten('Ali') == 'l'

def test_line():
    assert shorten('I love you') == ' lv y'

def test_numbers():
    assert shorten('Hello123') == 'Hll123'

def test_punctuation():
    assert shorten('Hello, there!') == 'Hll, thr!'
