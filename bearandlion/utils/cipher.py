from Crypto.Cipher import AES
from Crypto.Util import Counter


def create_cipher(key):
    return AES.new(key, AES.MODE_CTR,
                   counter=Counter.new(128, initial_value=0))


def encrypt(key, data):
    return create_cipher(key).encrypt(data)


def decrypt(key, data):
    return create_cipher(key).decrypt(data)
