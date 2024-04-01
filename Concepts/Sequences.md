---
tags:
  - calculus
  - series-sequences
---
# Sequences
- **Set of terms**
- Where $n$ is a positive integer
- $1$ is the assumed initial value for $n$ if it isn't given.
Notation 1:
$$a_{1} \,, a_{2} \,, a_{3} \dots$$


Notation 2:
$$
 \{ a_{n}\}_{n=k}^\infty
$$
### Sequence from function
Ex 1.
$$
\{ \,  \frac {-1^{n+1}2^n}{n+1} \,  \}
$$
a2 = 1
a3 = -4/3
a4 = 2
a5 = -16/5
a6 = 16/3

Ex 2.

$$
\{ \,   (-1)^n \sqrt{n-2} \, \}_{n=2}
$$
a2 = 0
a3 = -1
a4 = $\sqrt{2}$
a5 = $-\sqrt{3}$
a6 = $\sqrt{4}$


### Function/Formula from sequence
Find the function from the sequence.

Ex 1.

$$
\{a_n\} = \left( 2, \frac{3}{\sqrt{2}},\, \frac{4}{\sqrt{3}}, \frac{5}{2}  \ldots \right)
$$


Tips:
- Make all the terms have the same parttern.
- Give all terms have sqroots for example.

$$
\{a_n\} = \left( \frac{2}{\sqrt{1}}, \frac{3}{\sqrt{2}},\, \frac{4}{\sqrt{3}}, \frac{5}{\sqrt{4}}  \ldots \right)
$$
- Make each term relate to $n$.
  $$
a_{n} = \frac{n+1}{\sqrt{n}}
$$

Ex 2.
$$
\{a_n\} = \left( -1, \frac{1}{2}, -\frac{1}{6}, \frac {1}{24}, -\frac {1}{120}  \ldots \right)
$$
Solution:
$$
a_{n} = \frac {-1}{n!}
$$

Ex 3.
We can define sequences by being given fixed terms and define the sequence around those terms.
Recursive Sequence.

Suppose:
$$
a_{1} = 2, a_{2} = 4
$$
Find $a_{3}$
$$
a_{n+1} = 2a_{n} - a_{n-1}
$$
Use previous terms.
$$
a_{3} = 2(a_{2}) - a_{1}
$$

Result
$$
6 = 2(4) - 2
$$
Find $a_{4}$
$$
a_{4} = 2(a_{3}) - a_{2}
$$
Result
$$
8 = 2(6) - 4
$$
Function:
$$
\frac {-1^n}{n!}
$$

### Limits of Sequences

$$
\lim_{ n \to \infty } a_{n}
$$
What happens to our sequence as n approaches infinity? 
- Bigger?
- Smaller?
- Converges on a number?
- Infinity, -Infinity, DNE?

## [[Convergence]]
An infinite sum is the limit of the sequence of partial sums:
$$
\sum_{j=1 }^{\infty} a_j = \lim_{n \to \infty} \sum_{j=1}^{n} a_j
$$
When the limit exists we say the sum converges
## [[Divergence]]
Otherwise the sum is said to diverge

## [[Properties Of Sequences]]


## Geometric Sum

$$
S = \frac{a(1 - r^n)}{1 - r}
$$
## Harmonic Sum

$$
H_n = \sum_{k=1}^{n} \frac{1}{k}
$$
 
 