from plates import is_valid

def test_start_with_letter():
    assert is_valid("CS50") == True
    assert is_valid("7777") == False
def test_number_middle():
    assert is_valid("ha4rsh") == False
    assert is_valid("CS50P") == False
def test_number():
    assert is_valid("5555") == False
def test_length():
    assert is_valid("CS50") == True
    assert is_valid("A") == False
def test_alpanumeric():
    assert is_valid("PI3.13") == False
def test_zero_placement():
    assert is_valid("CD05") == False
