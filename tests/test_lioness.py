import binascii

from bearandlion import lioness


def test_encrypt():
    key = binascii.unhexlify(
        '00112233445566778899aabbccddeeff'
    )
    plaintext = binascii.unhexlify(
        '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
    )
    ciphertext = binascii.unhexlify(
        '7a489e392d483a5b2bce9581390fb47de862e9cc036ec24dab072dab8c88d2d7'
    )
    assert lioness.encrypt(key, plaintext) == ciphertext


def test_decrypt():
    key = binascii.unhexlify(
        '00112233445566778899aabbccddeeff'
    )
    plaintext = binascii.unhexlify(
        '000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f'
    )
    ciphertext = binascii.unhexlify(
        '7a489e392d483a5b2bce9581390fb47de862e9cc036ec24dab072dab8c88d2d7'
    )
    assert lioness.decrypt(key, ciphertext) == plaintext
