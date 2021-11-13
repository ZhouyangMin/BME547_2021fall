import pytest


@pytest.mark.parametrize("x1, y1, x2, y2, input_x, expected", [
    (1, 2, 3, 4, 5, 6), (2, 2, 4, 16, 7, 37), (3, 9, 7, 93, 1.6, -20.4)
])
def test_twopointform(x1, y1, x2, y2, input_x, expected):
    from twopointform import twopointform
    answer = twopointform(x1, y1, x2, y2, input_x)
    assert answer == expected
