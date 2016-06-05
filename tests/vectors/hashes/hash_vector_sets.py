"""
This file contains code taken from PyCA Cryptography [0]:

- `HashVectorSets.parse_vectors` is a modified version of their
  `tests.utils.load_hash_vectors`

Information regarding its license can be found in ../LICENSE.

[0]: https://github.com/pyca/cryptography
"""
import binascii

from ..vector_sets import VectorSets


class HashVector:
    def __init__(self, message, digest):
        self.message = message
        self.digest = digest


class KeyedHashVector(HashVector):
    def __init__(self, message, digest, key):
        super(KeyedHashVector, self).__init__(message, digest)
        self.key = key


class HashVectorSets(VectorSets):
    @classmethod
    def parse_vectors(cls, vector_lines):
        vectors = list()
        length = None
        key = None
        msg = None
        md = None
        for line in vector_lines:
            try:
                name, value = line.split(' = ')
            except ValueError:
                # ignore line that is not in the format `name = value`
                continue
            else:
                if name == 'Len':
                    # parse the provided length and catch an edge case in the
                    # NIST vectors, where an empty string is represented as hex
                    # 00, which is of course not actually an empty string
                    length = int(value)
                else:
                    try:
                        value = binascii.unhexlify(value)
                    except TypeError:
                        # ignore line with a value that fails to unhexlify
                        continue
                    else:
                        if name == 'Key':
                            key = value
                        elif name == 'Msg':
                            if length > 0:
                                msg = value
                            else:
                                msg = b''
                        elif name == 'MD':
                            md = value

                            # after MD is found, the vector is complete
                            if key is None:
                                vectors.append(HashVector(msg, md))
                            else:
                                vectors.append(KeyedHashVector(msg, md, key))
                                key = None
                            length = None
                            msg = None
                            md = None
        return vectors
