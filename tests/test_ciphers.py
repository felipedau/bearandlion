import binascii

import pytest

from bearandlion import errors, lioness


CIPHERS = [lioness]
CIPHERS_IDS = [c.__name__.split('.')[-1] for c in CIPHERS]


@pytest.fixture(params=CIPHERS, ids=CIPHERS_IDS)
def cipher(request):
    return request.param


def test_encrypt_decrypt(cipher):
    key = binascii.unhexlify(
        '00112233445566778899aabbccddeeff'
    )
    plaintext = binascii.unhexlify(
        '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
    )
    ciphertext = cipher.encrypt(key, plaintext)
    assert cipher.decrypt(key, ciphertext) == plaintext


OPERATIONS = ['encrypt', 'decrypt']
DATA_LENGTHS = range(4)


@pytest.mark.parametrize('data_length', DATA_LENGTHS)
@pytest.mark.parametrize('operation', OPERATIONS)
def test_data_length(cipher, operation, data_length):
    unit = binascii.unhexlify('00112233445566778899aabbccddeeff')
    data = unit * data_length
    is_short = data < unit * 2
    try:
        cipher.__dict__[operation](key=unit, data=data)
    except errors.ShortDataError:
        assert is_short
    else:
        assert not is_short
