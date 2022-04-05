"""
Coded by @majhcc
"""
import string
import random


def get_random_str(length):
    """
    Returns a random string of length characters.
    """
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
