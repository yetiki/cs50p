from twttr import shorten
import pytest

# --- Tests for shorten() ---
def test_shorten_with_int():
    with pytest.raises(TypeError):
        shorten(1)

def test_shorten_with_lowercase():
    assert shorten("happy new year") == "hppy nw yr"

def test_shorten_with_uppercase():
    assert shorten("MERRY CHRISTMAS") == "MRRY CHRSTMS"

def test_shorten_with_mixedcase():
    assert shorten("SeAsOnS gReEtInGs") == "SsnS gRtnGs"

def test_shorten_with_no_vowels():
    assert shorten("rhythm") == "rhythm"

def test_shorten_with_only_vowels():
    assert shorten("AEIOUaeiou") == ""

def test_shorten_with_only_spaces():
    assert shorten("   ") == "   "

def test_shorten_empty_string():
    assert shorten("") == ""

def test_shorten_with_punctuation():
    assert shorten("!\"£$%^&*()-_=+;:'@#~,<.>/?") == "!\"£$%^&*()-_=+;:'@#~,<.>/?"

def test_shorten_with_numbers():
    assert shorten("0123456789") == "0123456789"