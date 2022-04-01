import pytest

from simple_library_01.functions import get_month_days


def test_get_month_days():
    assert get_month_days(1930,1) == 30
    assert get_month_days(1960,2) == 29
    assert get_month_days(2022,2) == 28
    assert get_month_days(1960,3) == 31
    assert get_month_days(1960,4) == 30


    with pytest.raises(AttributeError):
        get_month_days(2012,0)
    
        




