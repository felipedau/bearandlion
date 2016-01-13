from Crypto.Hash import SHA256
from Crypto.Util.strxor import strxor


def hash(data):
    h = SHA256.new()
    h.update(data)
    return h.digest()


def xor(str1, str2):
    assert len(str1) == len(str2)
    return strxor(str1, str2)
