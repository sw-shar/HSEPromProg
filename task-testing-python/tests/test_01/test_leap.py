import pytest

from simple_library_01.functions import is_leap


def test_is_leap():
    assert not is_leap(2022)
    assert not is_leap(1)
    assert not is_leap(2100)
    assert is_leap(2060)
    assert not is_leap(2062)
    assert is_leap(2068)
    assert is_leap(400)

    with pytest.raises(AttributeError):
        is_leap(0)
    
        



