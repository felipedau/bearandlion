"""
This file contains code taken from PyCA Cryptography [0]:

- `CipherVectorSets.parse_vectors` is a modified version of their
  `tests.utils.load_nist_vectors`

Information regarding its license can be found in ../LICENSE.

[0]: https://github.com/pyca/cryptography
"""
import binascii

from ..vector_sets import VectorSets


class CipherVector:
    def __init__(self, key, iv, plaintext, ciphertext):
        self.key = key
        self.iv = iv
        self.plaintext = plaintext
        self.ciphertext = ciphertext


class CipherVectorSets(VectorSets):
    @classmethod
    def parse_vectors(cls, vector_lines):
        vectors = list()
        key = None
        iv = None
        plaintext = None
        ciphertext = None
        for line in vector_lines:
            try:
                name, value = line.split(' = ')
                value = binascii.unhexlify(value)
            except (ValueError, TypeError):
                # ignore line that is not in the format `name = value` or has a
                # value that fails to unhexlify
                continue
            else:
                if name == 'KEY':
                    key = value
                elif name == 'IV':
                    iv = value
                elif name == 'PLAINTEXT':
                    plaintext = value
                elif name == 'CIPHERTEXT':
                    ciphertext = value

                    # after CIPHERTEXT is found, the vector is complete
                    vectors.append(
                        CipherVector(key, iv, plaintext, ciphertext))
                    key = None
                    iv = None
                    plaintext = None
                    ciphertext = None
        return vectors
