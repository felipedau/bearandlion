from Crypto.Cipher import AES
from Crypto.Util import number


class XCounter:
    # Implements a string counter to do AES-CTR mode
    i = 0

    def __init__(self, size):
        self.size = size

    def __call__(self):
        ii = number.long_to_bytes(self.i)
        ii = '\x00' * (self.size-len(ii)) + ii
        self.i += 1
        return ii


def create_cipher(key):
    return AES.new(key, AES.MODE_CTR,
                   counter=XCounter(len(key)))


def encrypt(key, data):
    return create_cipher(key).encrypt(data)


def decrypt(key, data):
    return create_cipher(key).decrypt(data)
