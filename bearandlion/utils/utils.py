from Crypto.Hash import SHA256
from Crypto.Util.strxor import strxor

from .. import errors


def check_data_length(data_length, key_length):
    if data_length < key_length * 2:
        raise errors.ShortDataError()


def hash(data):
    h = SHA256.new()
    h.update(data)
    return h.digest()


def xor(str1, str2):
    return strxor(str1, str2)
