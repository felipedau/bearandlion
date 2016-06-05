from Crypto.Cipher import AES
from Crypto.Util import Counter


def create_cipher(key, iv=None):
    if iv is None:
        iv = 0
    return AES.new(key, AES.MODE_CTR,
                   counter=Counter.new(128, initial_value=iv))


def encrypt(key, data, iv=None):
    return create_cipher(key, iv).encrypt(data)


def decrypt(key, data, iv=None):
    return create_cipher(key, iv).decrypt(data)
