from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("pytest") == "pytst"
def test_uppercase():
    assert shorten("HARSH") == "HRSH"
def test_numbers():
    assert shorten("cs50") == "cs50"
def test_punctuation():
    assert shorten("hey, amit") == "hy, mt"

