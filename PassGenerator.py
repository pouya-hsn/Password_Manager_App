from random import sample
from string import ascii_letters

letters = ascii_letters
nums = '0123456789'
spe = '!@#$%&*_-'
symbols = letters + nums + spe


def generate(length):
    if type(length) == int:
        password = ''.join(sample(symbols, length))
    else:
        password = ''.join(sample(symbols, int(length)))
    return password
