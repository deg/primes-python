"""
CLI application for working with prime factorization.

Usage:
    $ primes --upto 100

This will compute the prime factors for each natural number from 2 to the specified upper limit.
"""

import click


def prime_factors(n):
    """
    Generate the prime factors of a number as a list of tuples (factor, count).

    Args:
        n (int): The number to factorize.

    Returns:
        list[tuple[int, int]]: A list of (factor, count) tuples representing the prime factorization.

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


@click.command()
@click.option("--upto", type=int, required=True, help="Compute prime factors for numbers up to this limit.")
def primes(upto):
    """
    CLI entry point to compute prime factors for numbers from 2 up to the specified limit.

    Args:
        upto (int): The upper limit for computing prime factors.
    """
    for number in range(2, upto + 1):
        factors = prime_factors(number)
        click.echo(f"{number}: {factors}")


if __name__ == "__main__":
    primes()
