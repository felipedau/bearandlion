import pytest

from bearandlion.utils import cipher, hash, xor

from .vectors.hashes.sha256.sha256_vector_sets import Sha256VectorSets


AES_ACCEPTED_KEY_LENGTHS = [16, 24, 32]


@pytest.fixture(params=AES_ACCEPTED_KEY_LENGTHS)
def key_length(request):
    return request.param


def test_aes_accepted_key_length(key_length):
    cipher.create_cipher(key=b'\x00'*key_length)


def test_aes_counter_length_based_on_key(key_length):
    key = b'\x00' * key_length
    plaintext = b'\x01' * key_length
    ciphertext = cipher.encrypt(key, plaintext)
    cipher.decrypt(key, ciphertext)


SHA256_VECTOR_SETS = Sha256VectorSets.parse_vector_sets()


@pytest.mark.parametrize('vector_set', SHA256_VECTOR_SETS.keys())
def test_sha256_vector_set(vector_set):
    for vector in SHA256_VECTOR_SETS[vector_set]:
        assert hash(vector.message) == vector.digest


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
