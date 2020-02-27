#!/usr/bin/env python3
from random import SystemRandom
from base64 import b64encode


ALT = '$!'
NUM = '0123456789'
CONFUSING = 'Il0OoZzYy'
SIZE=12


def has_alts(s):
    return all(a in s for a in ALT)


def has_upper(s):
    return any(c.isupper() for c in s)


def has_lower(s):
    return any(c.islower() for c in s)


def has_number(s):
    return any(c in NUM for c in s)


def no_confusing(s):
    return all(c not in CONFUSING for c in s)


if __name__ == '__main__':
    r = SystemRandom()
    while True:
        pwd_int = r.randrange(2**(SIZE*8))
        pwd = b64encode(
            pwd_int.to_bytes(SIZE, 'little'), altchars=ALT.encode('ascii')
        ).decode('ascii')
        if (
            has_alts(pwd) and
            has_upper(pwd) and
            has_lower(pwd) and
            has_number(pwd) and
            no_confusing(pwd)
        ):
            break

    print(pwd)
