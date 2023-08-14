from exercicio5 import *
import unittest

class TestExercicio5Methods(unittest.TestCase):

    def testSum(self):
        self.assertEqual(sum([1,2,2,1,5]), 11)

    def testMultiply(self):
        self.assertEqual(multiply([1,2,2,1,5]), 11)

if __name__ == '__main__':
    unittest.main()