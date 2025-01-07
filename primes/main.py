"""
CLI application to play with prime factorization groups.

Usage:
    $ primes --upto 100

This will compute the prime factors and shapes for each natural number up to the specified limit.
"""

import click


def prime_factors(n):
    """
    Generate the prime factors of a number as a list of (factor, count) tuples.

    Args:
        n (int): The number to factorize.

    Returns:
        list[tuple[int, int]]: A list of (factor, count) tuples showing the prime factorization.

    Examples:
        prime_factors(10) -> [(2, 1), (5, 1)]
        prime_factors(200) -> [(2, 3), (5, 2)]
    """
    factors = []
    divisor = 2
    while n > 1:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
        divisor += 1
    return factors


def shape(n):
    """
    Determine the shape of a number's prime factorization as a tuple of counts.

    Args:
        n (int): The number to compute the shape for.

    Returns:
        tuple[int]: A tuple of prime factor counts, sorted in descending order.

    Examples:
        shape(10) -> (1, 1)  # 10 = 2^1 * 5^1
        shape(50) -> (2, 1)  # 50 = 2^1 * 5^2
        shape(30) -> (1, 1, 1)  # 30 = 2^1 * 3^1 * 5^1
    """
    factors = prime_factors(n)
    counts = [count for _, count in factors]
    return tuple(sorted(counts, reverse=True))


@click.command()
@click.option("--upto",
              type=int,
              required=True,
              help="Compute prime factors and shapes up to this limit.")
def primes(upto):
    """
    CLI entry point to compute prime factors and shapes.

    Args:
        upto (int): The upper limit for computing prime factors and shapes.
    """
    for number in range(2, upto + 1):
        factors = prime_factors(number)
        factor_shape = shape(number)
        click.echo(f"{number}: factors={factors}, shape={factor_shape}")


if __name__ == "__main__":
    primes()
