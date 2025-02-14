"""
CLI application to play with prime factorization groups.

Usage:
    $ primes --upto 100

This will compute the prime factors and shapes for each natural number up to the specified limit.
"""

from collections import Counter
from functools import lru_cache

import click
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter
from matplotlib.ticker import FuncFormatter
import numpy as np


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
    help="Compute prime factors and shapes up to this number.",
)
@click.option(
    "--output",
    type=click.Choice(["list", "plot", "animate", "video-out"]),
    default="list",
    show_default=True,
    help="Specify the output format: list, plot, animate, or video-out.",
)
@click.option(
    "--top",
    type=int,
    default=20,
    show_default=True,
    help="Number of top shapes to display in the plot.",
)
def primes(start, end, output, top):
    """
    CLI entry point to compute prime factors and shapes.

    Args:
        start (int): The starting number for computation.
        end (int): The upper limit for computation.
        output (str): The type of output (list, plot, animate, video-out).
        top (int): Number of top shapes to display in plots or animations.
    """
    if output == "list":
        for number in range(start, end + 1):
            factors = prime_factors(number)
            factor_shape = shape(number)
            click.echo(f"{number}: factors={factors}, shape={factor_shape}")
    elif output == "plot":
        plot_distribution(start, end, top)
    elif output == "animate":
        animate_distribution(start, end, top)
    elif output == "video-out":
        animate_distribution(start, end, top, save_as_file=True)


@lru_cache(maxsize=None)
def prime_factors(n: int) -> list[tuple[int, int]]:
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
    if n <= 0:
        raise ValueError("Number must be greater than 0")

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
    if n > 1:
        factors.append((n, 1))
    return factors


def shape(n: int) -> list[int]:
    """
    Determine the shape of a number's prime factorization as a list of counts.

    Args:
        n (int): The number to compute the shape for.

    Returns:
        list[int]: A list of prime factor counts, sorted in descending order of exponent.

    Examples:
        shape(10) -> [1, 1]  # 10 = 2^1 * 5^1
        shape(250) -> [3, 1]  # 50 = 2^1 * 5^3
        shape(30) -> [1, 1, 1]  # 30 = 2^1 * 3^1 * 5^1
    """
    if n <= 0:
        raise ValueError("Number must be greater than 0")

    factors = prime_factors(n)
    counts = [count for _, count in factors]
    return sorted(counts, reverse=True)


def plot_distribution(start: int, end: int, top: int):
    """
    Plot the frequency distribution of prime factor shapes within a range.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        top (int): The number of top shapes to display.
    """
    # Calculate the frequency of each shape
    counts = Counter(tuple(shape(n)) for n in range(start, end + 1))

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


def animate_distribution(
    start: int, end: int, top: int, interval=20, save_as_file: bool = False
):
    """
    Animate the frequency distribution of prime factor shapes with log-bucket frame selection.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        top (int): The number of top shapes to display.
        interval (int): Time between frames in milliseconds.
    """
    # Generate frames
    frame_points = generate_frames(start, end)

    # Prepare the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlabel("Prime Factor Shape")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Top {top} Prime Factor Shapes")

    def update(frame):
        # Incrementally compute shapes up to the current frame
        current_shapes = [tuple(shape(n)) for n in range(start, frame + 1)]
        counts = Counter(current_shapes)

        def key_by_count(x):
            return -x[1]

        def key_by_shape(x):
            return (len(x[0]), x[0])

        filtered = sorted(counts.items(), key=key_by_count)[:top]
        sorted_counts = sorted(filtered, key=key_by_shape)

        # Extract shapes and frequencies
        shapes = [str(list(s[0])) for s in sorted_counts]
        frequencies = [s[1] for s in sorted_counts]

        # Update the bar chart
        ax.clear()
        ax.bar(shapes, frequencies)
        ax.set_xticks(range(len(shapes)))
        ax.set_xticklabels(shapes, rotation=45, ha="right", fontsize=8)
        ax.set_xlabel("Prime Factor Shape")
        ax.set_ylabel("Frequency")
        ax.yaxis.set_major_formatter(
            FuncFormatter(lambda x, _: f"{int(x):,}")
        )  # Format Y-axis with commas
        ax.set_title(f"Top {top} Prime Factor Shapes (N = {start} to {frame})")

    # The `ani` object must be retained to prevent garbage collection.
    ani = FuncAnimation(  # noqa: F841
        fig, update, frames=frame_points, interval=interval, repeat=False
    )

    plt.tight_layout()

    if save_as_file:
        click.echo("Generating video. Please wait...")
        ani.save("video-out.mp4", writer=FFMpegWriter(fps=10))
        click.echo("Video saved as 'video-out.mp4'.")
    else:
        plt.show()


def generate_frames(start, end, max_frames_per_bucket=250) -> list[int]:
    """
    Generate frame points for animation using logarithmic buckets.

    Args:
        start (int): The starting number of the range.
        end (int): The ending number of the range.
        max_frames_per_bucket (int): Maximum number of frames per 10x growth.

    Returns:
        list[int]: A list of numbers representing frames to display.
    """
    frames = []
    current = start

    # Determine bucket boundaries (powers of 10)
    while current <= end:
        next_bucket = min(current * 10, end + 1)
        num_frames = min(max_frames_per_bucket, next_bucket - current)

        # Distribute frames evenly within this bucket
        frames += list(
            np.round(np.linspace(current, next_bucket - 1, num_frames)).astype(int)
        )
        current = next_bucket

    return sorted(set(frames))


if __name__ == "__main__":
    primes()
