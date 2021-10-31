import unittest

from syntax import *

class SyntaxTest(unittest.TestCase):

    def testBigLetter(self):
        self.assertEqual(CheckSyntax("O"), "Follows the syntax!")

    def testSmallLetter(self):
        self.assertEqual(CheckSyntax("o"), "Does not follow the syntax!")

    def testBigSmall(self):
        self.assertEqual(CheckSyntax("Pb"), "Follows the syntax!")

    def testSmallSmall(self):
        self.assertEqual(Checksyntax("pb"), "Does not follow the syntax!")

    def testWrongBigSmallNum(self):
        self.assertEqual(Checksyntax("Pb0"), "Does not follow the syntax!")

    def testRightBigSmallSingleNum(self):
        self.assertEqual(Checksyntax("Pb2"), "Follows the syntax!")

    def testRightBigSmallMultipleNum(self):
        self.assertEqual(Checksyntax("Pb237842738472"), "Follows the syntax!")




if __name__ == '__main__'
    unittest.main()