"""
CLI application to play with prime factorization groups.

Usage:
    $ primes --upto 100

This will compute the prime factors and shapes for each natural number up to the specified limit.
"""

import click
import matplotlib.pyplot as plt
from collections import Counter


@click.command()
@click.option(
    "--start",
    type=int,
    default=2,
    show_default=True,
    help="Start computing prime factors and shapes from this number.",
)
@click.option(
    "--end",
    type=int,
    default=1000,
    show_default=True,
    help="Compute prime factors and shapes up to this limit.",
)
@click.option(
    "--plot",
    is_flag=True,
    help="Plot the frequency distribution of prime factor shapes.",
)
@click.option(
    "--top",
    type=int,
    default=20,
    show_default=True,
    help="Number of top shapes to display in the plot.",
)
def primes(start, end, plot, top):
    """
    CLI entry point to compute prime factors and shapes.

    Args:
        start (int): The starting number for computation.
        end (int): The upper limit for computation.
        plot (bool): Whether to plot the frequency distribution of shapes.
        top (int): Number of top shapes to display in the plot.
    """
    if plot:
        plot_distribution(start, end, top)
    else:
        for number in range(start, end + 1):
            factors = prime_factors(number)
            factor_shape = shape(number)
            click.echo(f"{number}: factors={factors}, shape={factor_shape}")


def prime_factors(n):
    """
    Generate the prime factors of a number as a list of (factor, count) tuples.

    This function computes the factors directly using trial division.

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
    while divisor * divisor <= n:
        count = 0
        while n % divisor == 0:
            n //= divisor
            count += 1
        if count > 0:
            factors.append((divisor, count))
        divisor += 1
    if n > 1:  # If n is a prime number larger than the square root of the original number
        factors.append((n, 1))
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


def plot_distribution(start, end, top):
    """
    Plot the frequency distribution of prime factor shapes within a range.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        top (int): The number of top shapes to display.
    """
    # Calculate the frequency of each shape
    counts = Counter(shape(n) for n in range(start, end + 1))

    # Sort shapes by descending frequency
    sorted_shapes = sorted(counts.items(), key=lambda x: -x[1])

    # Limit to the top `top` shapes
    top_shapes = sorted_shapes[:top]
    shapes, frequencies = zip(*top_shapes)

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(shapes)), frequencies, tick_label=[str(s) for s in shapes])
    plt.xlabel("Prime Factor Shape")
    plt.ylabel("Frequency")
    plt.title(f"Top {top} Prime Factor Shapes (N = {start} to {end})")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    primes()
