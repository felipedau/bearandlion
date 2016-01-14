from .utils import cipher, hash, xor


def encrypt(key, data):
    k = len(key)
    assert len(data) >= k * 2

    # Round 1
    r1 = xor(hash(data[k:]+key+'1')[:k], data[:k]) + data[k:]

    # Round 2
    k2 = xor(r1[:k], key)
    r2 = r1[:k] + cipher.encrypt(k2, r1[k:])

    # Round 3
    r3 = xor(hash(r2[k:]+key+'3')[:k], r2[:k]) + r2[k:]

    # Round 4
    k4 = xor(r3[:k], key)
    r4 = r3[:k] + cipher.encrypt(k4, r3[k:])

    return r4


def decrypt(key, data):
    k = len(key)
    assert len(data) >= k * 2

    r4 = data

    # Round 4
    k4 = xor(r4[:k], key)
    r3 = r4[:k] + cipher.decrypt(k4, r4[k:])

    # Round 3
    r2 = xor(hash(r3[k:]+key+'3')[:k], r3[:k]) + r3[k:]

    # Round 2
    k2 = xor(r2[:k], key)
    r1 = r2[:k] + cipher.decrypt(k2, r2[k:])

    # Round 1
    r0 = xor(hash(r1[k:]+key+'1')[:k], r1[:k]) + r1[k:]

    return r0
