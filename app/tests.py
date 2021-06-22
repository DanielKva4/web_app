import unittest

from django.test import TestCase
from unittest import *

class Tests(unittest.TestCase):
    def test_div(self):
        result = div_t([3, 6, 5, 7], [7, 5, 4, 8])
        self.assertTrue(result == [5, 7])

    def test_div2(self):
        result = div_t2([5, 4, 3, 2, 2, 1, 7, 5, 7, 4, 3, 3, 2])
        self.assertTrue(result == [5, 4, 3, 2, 1, 71])

def div_t(ls, ls2):
    result = []
    for x in ls:
        if x in ls2:
            result.append(x)
    return result


def div_t2(ls):
    result = []
    for x in ls:
        if x not in result:
            result.append(x)
    return result



if __name__ == '__main__':
    unittest.main()