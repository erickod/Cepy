import unittest

from cepy.transforms.zfill import CepFillTransform
from cepy.transforms.remove_non_digits import RemoveNonDigitsTransform

class TestTransforms(unittest.TestCase):

    def test_cep_fill(self, cep='123'):
        self.assertEqual(CepFillTransform.transform(cep), '00000123')
    
    def test_cep_fill_return(self, cep=1):
        self.assertEqual(type(CepFillTransform.transform(cep)), str)
    
    def test_remove_non_digits(self, cep='^ a7 3 7 0 0-000a.;/.\\-=-²*+@#'):
        self.assertEqual(RemoveNonDigitsTransform.transform(cep), '73700000')

if __name__ == '__main__':
    unittest.main()