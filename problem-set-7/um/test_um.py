from um import count

def test_empty():
    assert count("") == 0

def test_um_in_substring():
    assert count("sum") == 0
    assert count("jump") == 0
    assert count("human") == 0
    assert count("number") == 0
    assert count("maximum") == 0
    assert count("umbrella") == 0

def test_um_case_sensitivity():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1

def test_non_um_words():
    assert count("foo") == 0
    assert count("hello") == 0
    assert count("world") == 0

def test_punctuation():
    assert count("um.") == 1
    assert count("!um") == 1
    assert count("um,") == 1
    assert count("?.um") == 1

def test_um_in_sentence():
    assert count("hello, um, world") == 1
    assert count("This is a um, a test.") == 1
    assert count("Um, this is a test.") == 1
    assert count("This is a test um.") == 1
    assert count("Um, this, um... This is a, uh... Um... Umm This is a test!") == 3