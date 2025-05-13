from plates import is_valid


def test_is_valid_length():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("ABCdEFg") == False
    assert is_valid("Hello") == True


def test_is_valid_start():
    assert is_valid("A1") == False
    assert is_valid("B!") == False
    assert is_valid("CS") == True


def test_is_valid_end():
    assert is_valid("AB@12") == False
    assert is_valid("bAD_G") == False
    assert is_valid("ABc1") == True


def test_is_valid_loop():
    assert is_valid("AB012") == False
    assert is_valid("BA12A") == False
    assert is_valid("ABC123") == True