import unittest

from primes.main import prime_factors, shape


class TestPrimeFactors(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(prime_factors(10), [(2, 1), (5, 1)])
        self.assertEqual(prime_factors(50), [(2, 1), (5, 2)])
        self.assertEqual(prime_factors(30), [(2, 1), (3, 1), (5, 1)])
        self.assertEqual(prime_factors(1), [])  # 1 has no prime factors
        self.assertEqual(prime_factors(2), [(2, 1)])
        self.assertEqual(prime_factors(27), [(3, 3)])  # 27 = 3^3

    def test_prime_factors_large(self):
        """Test factorizations for larger numbers."""
        self.assertEqual(prime_factors(1000), [(2, 3), (5, 3)])  # 1000 = 2^3 * 5^3
        self.assertEqual(prime_factors(104729), [(104729, 1)])  # Large prime number
        self.assertEqual(
            prime_factors(13195), [(5, 1), (7, 1), (13, 1), (29, 1)]
        )  # 13195 = 5 * 7 * 13 * 29

    def test_prime_factors_edge_cases(self):
        """Test edge cases."""
        with self.assertRaises(ValueError):
            prime_factors(-1)  # Negative numbers not supported
        with self.assertRaises(ValueError):
            prime_factors(0)  # 0 is not valid for factorization

    def test_shape(self):
        """Test basic shapes."""
        self.assertEqual(shape(10), (1, 1))  # 10 = 2^1 * 5^1
        self.assertEqual(shape(50), (2, 1))  # 50 = 2^1 * 5^2
        self.assertEqual(shape(30), (1, 1, 1))  # 30 = 2^1 * 3^1 * 5^1
        self.assertEqual(shape(8), (3,))  # 8 = 2^3
        self.assertEqual(shape(1), ())  # 1 has no shape (no prime factors)

    def test_shape_large(self):
        """Test shapes for larger numbers."""
        self.assertEqual(shape(1000), (3, 3))  # 1000 = 2^3 * 5^3
        self.assertEqual(shape(13195), (1, 1, 1, 1))  # 13195 = 5 * 7 * 13 * 29
        self.assertEqual(shape(104729), (1,))  # Large prime number = 1^1

    def test_shape_edge_cases(self):
        """Test edge cases."""
        with self.assertRaises(ValueError):
            shape(-1)  # Negative numbers not supported
        with self.assertRaises(ValueError):
            shape(0)  # 0 is not valid for factorization


if __name__ == "__main__":
    unittest.main()
