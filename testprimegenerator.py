import unittest
from primegenerator import get_prime_numbers
import logging as log
class TestPrimeGenerator(unittest.TestCase):
    
    def test_isnumber(self):
        self.assertEqual(get_prime_numbers(''), 'Undefined')
        
    def test_isnegative(self):
        self.assertEqual(get_prime_numbers(-3), 'Undefined')
 
    def test_isdecimal(self):
        self.assertEqual(get_prime_numbers(''), 'Undefined')

    def test_iszero(self):
        self.assertEqual(get_prime_numbers(0), 'Undefined')

    def test_isone(self):
        self.assertEqual(get_prime_numbers(1), 'Undefined')

    def test_isvalid(self):
        self.assertEqual(get_prime_numbers(50), 
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

if __name__ == '__main__':
    unittest.main()