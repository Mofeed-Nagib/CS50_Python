from twttr import shorten


def test_shorten():
    assert shorten("Hello, world.") == "Hll, wrld."
    assert shorten("WHAT WOULD DAVID DO?") == "WHT WLD DVD D?"
    assert shorten("This Is CS50!") == "Ths s CS50!"
    assert shorten("aeiouAEIOU") == ""
    assert shorten("aAeEiIoOuU") == ""