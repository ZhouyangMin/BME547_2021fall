import pytest


@pytest.mark.parametrize("inputValue, expected", [
  
    ])

def test_twopointform(inputValue, expected):
    from twopointform import twopointform
    answer = twopointform(inputValue)
    assert answer == expected
