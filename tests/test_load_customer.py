import unittest
from ..src.jobs.load_customer import addition
# from ..src.jobs import load_customer
# from ..src import jobs

class TestAdditionFunction(unittest.TestCase):
    
    # Test for positive numbers
    def test_addition_positive_numbers(self):
        self.assertEqual(addition(3, 5), 8)
    
    # Test for negative numbers
    def test_addition_negative_numbers(self):
        self.assertEqual(addition(-3, -5), -8)
    
    # Test for mixed positive and negative numbers
    def test_addition_mixed_numbers(self):
        self.assertEqual(addition(-3, 5), 2)
    
    # Test for zero
    def test_addition_with_zero(self):
        self.assertEqual(addition(0, 5), 5)
        self.assertEqual(addition(5, 0), 5)
        self.assertEqual(addition(0, 0), 0)
    
    # Test for floating-point numbers
    def test_addition_floats(self):
        self.assertAlmostEqual(addition(3.5, 2.5), 6.0)
        self.assertAlmostEqual(addition(-3.5, -2.5), -6.0)
    
    # Test for large numbers
    def test_addition_large_numbers(self):
        self.assertEqual(addition(10**6, 10**6), 2 * 10**6)
    
    # Test for edge cases (like very small or very large values)
    def test_addition_edge_cases(self):
        self.assertEqual(addition(1, -1), 0)
        self.assertEqual(addition(-1, 1), 0)
        # Test for edge cases (like very small or very large values)
    def test_addition_invalid_param(self):
        with self.assertRaises(TypeError):
            addition('1', -1)
        with self.assertRaises(TypeError):
            addition('dfd', 'fdf')    

if __name__ == '__main__':
    unittest.main()