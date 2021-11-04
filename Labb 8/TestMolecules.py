import unittest

from syntax import *


class SyntaxTest(unittest.TestCase):
    def testCorrectCases(self):
        inputs = ['H10', 'H2', 'Fe12', 'Ag21', 'H10100']
        for e in inputs:
            self.assertEqual(CheckSyntax(e), 'Formeln är syntaktiskt korrekt')

    def testWrongCases(self):
        inputs = ['a', 'cr12', '8', 'Cr0', 'Pb1', 'H01011']
        expected_output = ['Saknad stor bokstav vid radslutet a',
                           'Saknad stor bokstav vid radslutet cr12',
                           'Saknad stor bokstav vid radslutet 8',
                           'För litet tal vid radslutet ',
                           'För litet tal vid radslutet ',
                           'För litet tal vid radslutet 1011']
        for i in range(len(inputs)):
            self.assertEqual(CheckSyntax(inputs[i]), expected_output[i])


if __name__ == '__main__':
    unittest.main()