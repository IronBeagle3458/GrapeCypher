from types import new_class
from typing import NewType
import unittest
import New_Grape

class GrapeTesting(unittest.TestCase):
    def test_encrypt(self):
        string = New_Grape.encrypt('a ', [2, 2, 1])
        self.assertEqual(string, 'a?c')
        
    def test_decrypt(self):
        string = New_Grape.decrypt('a?c', [2, 2, 1])
        self.assertEqual(string, 'a ')

unittest.main()