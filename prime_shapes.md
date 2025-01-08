# Mathematics of Prime Factor Shapes

This document describes the math behind this demo, including **prime factorization** and "**shapes**".

---

## 1. Prime Factorization

Prime factorization is the process of breaking down a number into a product of prime numbers. Every positive integer greater than 1 has a unique prime factorization.

### Example

- 10 = 2¹ × 5¹
- 50 = 2¹ × 5²
- 200 = 2³ × 5²

In this program, we express **prime factors** as pairs (p, k), where:

- `p` is a prime number.
- `k` is the exponent of `p` in the factorization.

For example:

- 10 → `[(2, 1), (5, 1)]`
- 50 → `[(2, 1), (5, 2)]`
- 200 → `[(2, 3), (5, 2)]`

---

## 2. Prime Factor Shapes

We've invented the term **shape** to describe classes of numbers. The shape of a number is defined as the **sorted list of the exponents** of its prime factors.

### Definition

For a number `n`, if its prime factorization is:

`n = p₁ᵏ¹ × p₂ᵏ² × ... × pₘᵏᵐ`

then the **shape** of `n` is:

`shape(n) = sorted([k₁, k₂, ..., kₘ], descending)`

### Examples

- 10 = 2¹ × 5¹ → `shape(10) = [1, 1]`
- 50 = 2¹ × 5² → `shape(50) = [2, 1]`
- 200 = 2³ × 5² → `shape(200) = [3, 2]`

---

## 3. Distribution of Prime Factor Shapes

It's well known that the number of primes less than a large number `n` asymptotically approaches `n/log(n)`. Or, in our terms, that is the count of numbers less than `n` that are in shape class `[1]`.

Let's call `Ξ(c, n)` the count of numbers less than `n` that are in class `c`.

So `Ξ([1], n)` ~= `n/log(n)`

It seems clear that `Ξ([2], n)` is much less, since squares of primes are more widely spaced than the original primes.
Similarly, `Ξ([1,1], n)` should be much greater, since products of two primes are much closer spaced than the original primes.

But, the exact relationship is not clear, since for any given `n`, the number of members of these more complex classes is dependent on the relationships between only much smaller numbers.

I don't have the math background to tackle this properly. This program, therefore, is just a first attempt at visualizing the relative sizes of the classes as `n` grows.

---

## 4. Visualization

To better understand the distribution, the program generates:

1. **Frequencies**: Counts how many numbers share a specific shape within a given range.
2. **Bar Charts**: Visual representations of the most common shapes.
3. **Animations**: Evolving distributions as the range increases.

### Example

For numbers up to 10, the shapes and their frequencies are:

| Shape  | Frequency | Numbers |
|--------|-----------|---------|
| []     | 1         | 1       |
| [1]    | 4         | 2,3,5,7 |
| [1, 1] | 2         | 6,10    |
| [2]    | 2         | 4,9     |
| [3]    | 1         | 8       |

---

## 5. Further Reading

- [Prime Factorization (Wikipedia)](https://en.wikipedia.org/wiki/Prime_factorization)
- [Distribution of Prime Numbers](https://en.wikipedia.org/wiki/Distribution_of_prime_numbers)
