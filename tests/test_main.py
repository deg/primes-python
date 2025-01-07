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

    def test_shape(self):
        self.assertEqual(shape(10), (1, 1))  # 10 = 2^1 * 5^1
        self.assertEqual(shape(50), (2, 1))  # 50 = 2^1 * 5^2
        self.assertEqual(shape(30), (1, 1, 1))  # 30 = 2^1 * 3^1 * 5^1
        self.assertEqual(shape(8), (3,))  # 8 = 2^3
        self.assertEqual(shape(1), ())  # 1 has no shape (no prime factors)


if __name__ == "__main__":
    unittest.main()
