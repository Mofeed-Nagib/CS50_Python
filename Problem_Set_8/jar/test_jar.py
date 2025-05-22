import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(6)
    assert jar.capacity == 6

    with pytest.raises(ValueError, match="Capacity must be non-negative"):
        Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(5)
    assert str(jar) == "🍪" * 5


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10

    with pytest.raises(ValueError, match="Too many cookies to deposit"):
        jar.deposit(3)

    with pytest.raises(ValueError, match="Cannot deposit a negative number of cookies"):
        jar.deposit(-1)

    jar.deposit(0)
    assert jar.size == 10


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(5)
    assert jar.size == 4

    with pytest.raises(ValueError, match="Too many cookies to withdraw"):
        jar.withdraw(5)

    with pytest.raises(ValueError, match="Cannot withdraw a negative number of cookies"):
        jar.withdraw(-1)

    jar.withdraw(0)
    assert jar.size == 4