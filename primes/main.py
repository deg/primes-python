"""
This module contains a command-line interface (CLI) application that interacts with users
and provides various utilities for greetings and calculations.

Features:

- Greet a user by name.
- Calculate the factorial of a number.
- Check if a number is prime.

Usage:
    Run this script from the command line with various commands and options.

Example:
    $ python main.py greet --name Alice
    Hello, Alice!

    $ python main.py factorial --number 5
    Factorial of 5 is 120.

    $ python main.py is-prime --number 17
    17 is a prime number.

Dependencies:
    click: A package for creating command-line interfaces.

Functions:
    greet(name: str): Greets the user by name.
    factorial(number: int): Calculates the factorial of a number.
    is_prime(number: int): Checks if a number is prime.
"""

import click
from math import factorial as math_factorial


@click.group()
def cli():
    """A command-line interface for greeting users and performing calculations."""
    pass


@cli.command()
@click.option("--name", default="World", help="Name to greet.")
def greet(name: str):
    """
    Greet the user by name.

    Args:
        name (str): The name of the user to greet. Defaults to "World".

    Example:
        $ python main.py greet --name Alice
        Hello, Alice!
    """
    click.echo(f"Hello, {name}!")


@cli.command()
@click.option("--number", type=int, required=True, help="Number to calculate the factorial of.")
def factorial(number: int):
    """
    Calculate the factorial of a number.

    Args:
        number (int): The number to calculate the factorial for. Must be a non-negative integer.

    Example:
        $ python main.py factorial --number 5
        Factorial of 5 is 120.
    """
    if number < 0:
        click.echo("Error: Factorial is only defined for non-negative integers.")
        return
    result = math_factorial(number)
    click.echo(f"Factorial of {number} is {result}.")


@cli.command(name="is-prime")
@click.option("--number", type=int, required=True, help="Number to check for primality.")
def is_prime(number: int):
    """
    Check if a number is prime.

    Args:
        number (int): The number to check for primality.

    Example:
        $ python main.py is-prime --number 17
        17 is a prime number.
    """
    if number < 2:
        click.echo(f"{number} is not a prime number.")
        return
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            click.echo(f"{number} is not a prime number.")
            return
    click.echo(f"{number} is a prime number.")


if __name__ == "__main__":
    cli()
