---
tags:
  - calculus
---

# Intro

The derivative of a function represents its **rate of change** at any given point. Geometrically, it corresponds to the slope of the tangent line to the graph of the function at that point .

$$\frac {d}{dx}[x^n]$$

- $f'(x)$
- Slope of tangent line

Velocity is the derivative position & acceleration the derivative of velocity

# Speed

How long does it take the beer to get to the flower?
Finding average speed is easy, rise over run.

![[Screenshot 2024-03-09 at 3.04.04 PM.png]]

# Velocity

Calculating how quickly a hive is falling at $(t)$ isn't easy though.
It's a factor of $(t)$.
![[falling.gif]]

# Definition

A function which evaluates the slope of a tangent line at point $x$ on a graph.

- Rate of change.
- Usually expressed as a function.
- Slope of the tangent line at a point, x.
- Functions that evaluate to slope of an original function at some value, usually x.
  - Original Function: $f(x)$
    - Derivative: $f^1(x)$
    - Evaluates to slope of $f(x)$
- Calculus in a nutshell, understanding how to represent infinitesimally small numbers
  - Area of square
    ![[Screenshot 2024-03-08 at 1.28.52 AM.png]]
  - Volume of a cube
    ![[Screenshot 2024-03-08 at 1.27.45 AM.png]]

## Equation of the tangent line

$y = f(a) + f'(a)(x-a)$

## The Prime Notation

How to represent infinitesimally small numbers?

$f'(a)$ is derived from taking the limit of the difference quotient at a. For that reason we also call slope of the tangent line

$$
f'(a) = \lim_{ n \to a } \frac {f(b) - f(a)}{b-a}
$$

is the derivative of $f(x)$ at $x = a$.

$$
\frac {{df}}{dx}\mid_{x=a} = \lim_{ b \to a } \frac {f(b) - f(a)}{b-a}
$$

- Think of $dx$ as a small change to x.
- Think of $df$ as a small change resulting from change of $x/a$.
- Think of ${df}{dx}$ as the ratio of change.
  ![[Screenshot 2024-03-08 at 1.02.09 AM.png]]

# Finding Derivatives

How to go from $f(x)$ to $f'(x)$?

1. $f(x)=x^4−2x^2+1$
2. $f^1(x) = 4x^3-4x$

- [[First Principles]]
- [[Difference Quotient]]
- [[Derivative Rules]]

# Applications

Knowing derivatives represent a max & min of the line what can they do for us?

> $f'(x)$ are mins & max's of a graph.

- Identify faces in a crowd
- Predict traffic patterns in a major city

We can use the

- [[First Derivative Test]]
- [[Second Derivative Test]]

# Application

Maximizing revenue for sales of a product.

- Price cheap means more units but less revenue per unit.
- Price expensive means less units but more revenue per unit.
  We'll use $f^1s$ to calculate the optimized price.

Finding the minimized value is also useful

[[Second Derivatives]]

## [[Derivatives of Angles]]
