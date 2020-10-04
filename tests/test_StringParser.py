from StringParser.StringParser import StringParser

def test_is_valid_text():
    sp = StringParser("strings.txt")
    r = sp.is_valid_text("xyyx")
    assert r is True

def test_is_invalid_text():
    sp = StringParser("strings.txt")
    r = sp.is_valid_text("xyxx")
    assert r is False

def test_valid_string_count():
    sp = StringParser("strings.txt")
    r = sp.get_valid_line_count()
    assert r == 3
