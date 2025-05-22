import pytest
from seasons import age_minutes

def test_age_minutes():
    with pytest.raises(SystemExit, match="Invalid date"):
        age_minutes("2200-12-12")
    with pytest.raises(SystemExit, match="Invalid date"):
        age_minutes("123456789")
    with pytest.raises(SystemExit, match="Invalid date"):
        age_minutes("hello, world")
