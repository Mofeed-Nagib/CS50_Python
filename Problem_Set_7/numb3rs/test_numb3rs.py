from numb3rs import validate

def test_validate_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("1.12.123.234") == True
    assert validate("222.22.2.0") == True

def test_validate_false():
    assert validate("-1.-1.-1.-1") == False
    assert validate("255.256.257.258") == False
    assert validate("1.12.123.1234.12345") == False
    assert validate("cat") == False