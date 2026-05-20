from twttr import shorten

def test_word():
    assert shorten('Fizaan') == 'Fzn'
    assert shorten('Ali') == 'l'

def test_line():
    assert shorten('I love you') == ' lv y'

