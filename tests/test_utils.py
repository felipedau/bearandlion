import pytest

from bearandlion.utils import xor


DATA_LENGTHS = range(3)


@pytest.mark.parametrize('data_length2', DATA_LENGTHS)
@pytest.mark.parametrize('data_length1', DATA_LENGTHS)
def test_xor_data_length(data_length1, data_length2):
    if data_length1 != 0 and data_length2 != 0:
        unit = b'\x00'
        str1 = unit * data_length1
        str2 = unit * data_length2
        is_equal = len(str1) == len(str2)
        try:
            xor(str1, str2)
        except ValueError:
            assert not is_equal
        else:
            assert is_equal
