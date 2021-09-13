# hdl test
import pytest

@pytest.mark.parametrize('HDL_value, expected', [
    (65, 'Normal'),
    (45, 'borderline Low'),
    (15, 'Low')])

def test_hdl_analysis(HDL_value, expected):
    from blood_calculation import hdl_analysis
    answer = hdl_analysis(HDL_value)
    assert answer == expected
    
