from um import count

def test_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_um_zero():
    assert count("Hello, World!") == 0
    assert count("Umbrella") == 0
    assert count("UMPIRE TRUMP PLUM") == 0