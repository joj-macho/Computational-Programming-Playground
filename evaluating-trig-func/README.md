# Trigonometric Functions Evaluation

## Description

This Python program evaluates and compares trigonometric functions, including sine (sin), cosine (cos), arcsine (arcsin), arccosine (arccos), and tangent (tan) using different mathematical methods. The program includes power-series expansion and continued fraction representations to calculate these trigonometric functions.

**Power-Series Expansion**

Power series expansion is a mathematical method to approximate functions using an infinite series of terms. The trigonometric functions are approximated using Taylor series expansions. For sine (sin) and arcsine (arcsin):
$$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \cdots$$

The power series expansion for arcsin(x) is obtained by integrating the power series expansion of sin(x):
$$\arcsin(x) = x + \frac{1}{2} \frac{x^3}{3} + \frac{1}{2 \cdot 3} \frac{x^5}{5} + \cdots$$

The power series expansion for cos (cosine) is also a Taylor series:
$$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \cdots$$


**Continued Fraction Representation**

Continued fractions are another way to approximate functions as the quotient of two polynomials. The continued fraction for tan(x) is given by:
$$\tan(x) = \cfrac{x}{1-\cfrac{x^2}{3-\cfrac{x^2}{5-\cdots}}}$$

## How it Works

- The `main` function sets up test values for x (input values), which are 0.2, 0.5, and 0.8 in this case. The main function proceeds to calculate and print the results of various trigonometric functions for each x.

- The `sine` and `cosine` functions evaluate sine (sin) and cosine (cos) using their respective power-series expansions. The functions use iterations to add up terms in the series until the desired precision (`eps`) is reached.

- The `arcsine` function evaluates arcsine (arcsin) using its power-series expansion, which involves integrating the power series expansion of sine. The `arccosine` function calculates arccosine (arccos) by subtracting arcsin from $\frac{\pi}{2}$.

- The `tangent_power_series` function calculates tangent (tan) using its power-series expansion. It iteratively adds up terms in the series.

- The `tangent_continued_fraction` function calculates tangent (tan) using its continued fraction representation. This function utilizes a loop to compute the terms of the continued fraction until the desired precision is achieved.

## Program Input & Output

When you run the program, `trig_evaluation.py`, the output will look like this;

```

Trigonometric Function Evaluation

Input value: x = 0.2

Real sin(x): 0.19866933079506122
sin(x) using power series expansion: 0.19866933079506124

Real cos(x): 0.9800665778412416
cos(x) using power series expansion: 0.9800665778412416

Real arcsin(x): 0.2013579207903308
arcsin(x) using power series expansion: 0.2013579207903308

Real arccos(x): 1.369438406004566
arccos(x) using power series expansion: 1.3694384060045657

Real tan(x): 0.2027100355086725
tan(x) using power series expansion: 0.201336002541094
tan(x) using continued fractions: 0.2027100355086725

--------------------------------

Input value: x = 0.5

Real sin(x): 0.479425538604203
sin(x) using power series expansion: 0.479425538604203

Real cos(x): 0.8775825618903728
cos(x) using power series expansion: 0.8775825618903728

Real arcsin(x): 0.5235987755982989
arcsin(x) using power series expansion: 0.5235987755982986

Real arccos(x): 1.0471975511965979
arccos(x) using power series expansion: 1.0471975511965979

Real tan(x): 0.5463024898437905
tan(x) using power series expansion: 0.5210953054937474
tan(x) using continued fractions: 0.5463024898437905

--------------------------------

Input value: x = 0.8

Real sin(x): 0.7173560908995228
sin(x) using power series expansion: 0.7173560908995229

Real cos(x): 0.6967067093471654
cos(x) using power series expansion: 0.6967067093471654

Real arcsin(x): 0.9272952180016123
arcsin(x) using power series expansion: 0.9272952180016

Real arccos(x): 0.6435011087932843
arccos(x) using power series expansion: 0.6435011087932966

Real tan(x): 1.0296385570503641
tan(x) using power series expansion: 0.8881059821876232
tan(x) using continued fractions: 1.0296385570503646

--------------------------------
```