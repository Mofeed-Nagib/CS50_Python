from bank import value


def test_value_hello():
    assert value("Hello, world.") == 0
    assert value("Hello, it's me.") == 0


def test_value_h():
    assert value("Howdy, friends!") == 20
    assert value("How is everyone doing?") == 20


def test_value():
    assert value("Good Morning!") == 100
    assert value("Welcome, all!") == 100