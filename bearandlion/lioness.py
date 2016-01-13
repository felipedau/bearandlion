from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util import number, strxor


def hash(data):
    h = SHA256.new()
    h.update(data)
    return h.digest()


def xor(str1, str2):
    assert len(str1) == len(str2)
    return strxor.strxor(str1, str2)


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


def encrypt(key, message):
    k = len(key)
    assert len(message) >= k * 2

    # Round 1
    r1 = xor(hash(message[k:]+key+'1')[:k], message[:k]) + message[k:]

    # Round 2
    k2 = xor(r1[:k], key)
    c = AES.new(k2, AES.MODE_CTR, counter=XCounter(k))
    r2 = r1[:k] + c.encrypt(r1[k:])

    # Round 3
    r3 = xor(hash(r2[k:]+key+'3')[:k], r2[:k]) + r2[k:]

    # Round 4
    k4 = xor(r3[:k], key)
    c = AES.new(k4, AES.MODE_CTR, counter=XCounter(k))
    r4 = r3[:k] + c.encrypt(r3[k:])

    return r4


def decrypt(key, message):
    k = len(key)
    assert len(message) >= k * 2

    r4 = message

    # Round 4
    k4 = xor(r4[:k], key)
    c = AES.new(k4, AES.MODE_CTR, counter=XCounter(k))
    r3 = r4[:k] + c.encrypt(r4[k:])

    # Round 3
    r2 = xor(hash(r3[k:]+key+'3')[:k], r3[:k]) + r3[k:]

    # Round 2
    k2 = xor(r2[:k], key)
    c = AES.new(k2, AES.MODE_CTR, counter=XCounter(k))
    r1 = r2[:k] + c.encrypt(r2[k:])

    # Round 1
    r0 = xor(hash(r1[k:]+key+'1')[:k], r1[:k]) + r1[k:]

    return r0
