import unittest

from syntax import *


class SyntaxTest(unittest.TestCase):
    def testKattisCases(self):
       # self.assertEqual(CheckSyntax('C'), 'Formeln är syntaktiskt korrekt')
        '''formulas = ['C(Xx4)5', 'C(OH4)C', 'C(OH4C', 'H2O)Fe', 'H0', 'H1C', 'H02C', 'Nacl', 'a', '(Cl)2)3', ')', '2']
        expected_outputs = ['Okänd atom vid radslutet 4)5', 'Saknad siffra vid radslutet C',
                            'Saknad högerparentes vid radslutet', 'Felaktig gruppstart vid radslutet )Fe',
                            'För litet tal vid radslutet', 'För litet tal vid radslutet C',
                            'För litet tal vid radslutet 2C', 'Saknad stor bokstav vid radslutet cl',
                            'Saknad stor bokstav vid radslutet a', 'Felaktig gruppstart vid radslutet )3',
                            'Felaktig gruppstart vid radslutet )', 'Felaktig gruppstart vid radslutet 2']
        for i in range(formulas):
            self.assertEqual(CheckSyntax(formulas[i]), expected_outputs[i])
'''
if __name__ == '__main__':
    unittest.main()
