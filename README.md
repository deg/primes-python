# Prime

This is a toy CLI Python project which I wrote mostly to learn VS Code tooling.

To give it some purpose, I've explored a math question that I've wondered about for a while: the relative frequency of different clasess of multiples of primes. For full details, see the accompanying [Prime Shapes](./prime_shapes.md) article.

You can also watch a [video](video-5m.mp4) that animates the changes in frequency.

## Installation

```bash
make install
```

This will set up a virtual environment and install all necessary dependencies.

## Running

### Basic Usage

The main command is `primes`, which computes prime factorizations and shapes for numbers in a given range.

```bash
primes [OPTIONS]
```

#### Options

* --start: Start computing prime factors and shapes from this number (default: 2).
* --end: Compute prime factors and shapes up to this number (default: 1000).
* --plot: Generate a bar chart showing the frequency distribution of prime factor shapes.
* --animate: Create an animation of the evolving distribution of prime factor shapes.
* --top: Specify the number of top shapes to display in plots or animations (default: 20).

### Examples

#### Compute Prime Factors and Shapes

To compute the prime factors and shapes of numbers from 2 to 100:

```bash
primes --start 2 --end 100
```

#### Plot the Distribution

To generate a bar chart of the most frequent prime factor shapes for numbers from 2 to 1000:

```bash
primes --plot --end 1000 --top 10
```

#### Animate the Distribution

To create an animation of the evolving distribution from 2 to 500:

```bash
primes --animate --end 500 --top 15
```

### Development

#### Testing

To run the test suite:

```bash
make test
```

This will run linting and unit tests.

### Linting

To check code quality with flake8:

```bash
make lint
```

## License

This code is available under the MIT license and may be used freely for any purposes.

However, if any research or papers come out of this, I request that this project and my name be cited.
