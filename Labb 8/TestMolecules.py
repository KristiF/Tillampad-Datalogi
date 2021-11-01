import unittest

from syntax import *

class SyntaxTest(unittest.TestCase):

    def testBigLetter(self):
        self.assertEqual(CheckSyntax("O"), "Formeln är syntaktiskt korrekt")

    def testSmallLetter(self):
        self.assertEqual(CheckSyntax("o"), "Saknade stor bokstav vid radslutet o")

    def testBigSmall(self):
        self.assertEqual(CheckSyntax("Pb"), "Formeln är syntaktiskt korrekt")

    def testSmallSmall(self):
        self.assertEqual(Checksyntax("pb"), "Saknade stor bokstav vid radslutet o")

    def testWrongBigSmallNum(self):
        self.assertEqual(Checksyntax("Pb0"), "För litet tal vid radslutet")

    def testRightBigSmallSingleNum(self):
        self.assertEqual(Checksyntax("Pb2"), "Formeln är syntaktiskt korrekt")

    def testRightBigSmallMultipleNum(self):
        self.assertEqual(Checksyntax("Pb237842738472"), "Formeln är syntaktiskt korrekt")

class SyntaxTest(unittest.TestCase):
    def testSingleCharAtom(self):
        self.assertTrue(CheckSyntax('H'))
        self.assertFalse(CheckSyntax('h'))
    def testMultiCharAtom(self):
        self.assertTrue(CheckSyntax('Ag'))
        self.assertFalse(CheckSyntax('aH'))
        self.assertTrue(CheckSyntax('Po'))
        self.assertFalse(CheckSyntax('123'))
    def testAtomNumber(self):
        self.assertTrue(CheckSyntax('Ag21'))
        self.assertTrue(CheckSyntax('H12344'))



if __name__ == '__main__':
    unittest.main()