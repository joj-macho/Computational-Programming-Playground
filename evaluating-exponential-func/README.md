# Exponential Function Evaluation

## Description

This Python program is designed to evaluate the exponential function $e^x$ for a set of input values using two different methods: power-series expansion and continued fraction representation.

**Power-Series Expansion**

The power-series expansion is one of the most fundamental methods for calculating the exponential function. It represents $e^x$ as an infinite sum:
$$e^x = \sum_{i=0}^{\infty} \frac{x^i}{i!} = 1 + x + \frac{x^2}{2!} + \cdots$$

The power series allows $e^x$ to be approximated by summing an infinite series of terms. In practice, only a finite number of terms are calculated, and the summation stops when the contribution of the next term is negligible.


**Continued Fraction Representation**

The continued fraction representation of $e^x$ is a different approach. It represents $e^x$ as a sequence of fractions:

This method provides a different perspective for calculating $e^x$ by recursively evaluating the numerators ($p_i$) and denominators ($1_i$) of the fractions. This representation is particularly useful when $x$ is small or when high precision is required.

## How it Works

- The `main` function evaluates the exponential function for a set of test values (`x_values`) and then prints the results for each method (power series and continued fraction). It also displays the input values and results.

- The `exponential_series` function calculates $e^x$ using the power-series expansion. It employs a loop to iteratively compute the series' terms and sum them. The function ensures that $e^x$ is accurately estimated, and if x is negative, it handles potential instabilities by taking the reciprocal of the result.

- The `exponential_continued_fraction` function calculates $e^x$ using its continued fraction representation. It iteratively evaluates the terms of the continued fraction until the desired level of precision is reached. Similar to the power-series method, this function also manages potential instability issues, ensuring accurate results.

## Program Input & Output

When you run the program, `exponential_evaluation.py`, the output will look like this;

```

Exponential Function Evaluation

Input value: x = 0.5

exp(x) using power series expansion: 1.6487212707001278
exp(x) using continued fraction representation: 1.6487212707001282

--------------------------------

Input value: x = 1.0

exp(x) using power series expansion: 2.7182818284590455
exp(x) using continued fraction representation: 2.718281828459046

--------------------------------

Input value: x = -0.5

exp(x) using power series expansion: 0.6065306597126335
exp(x) using continued fraction representation: 0.6065306597126334

--------------------------------
```