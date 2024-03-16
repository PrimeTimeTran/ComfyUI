---
tags:
  - calculus
---
![[calculus_score-sheet.png]]
# Intro
The mathematics of **change**. Find the rates of change and how that effects volume, area, and more.

- What does the tangent line represent?
- How does it relate to other points?
  
Calculus has numerous applications across various fields such as physics, engineering, economics, biology, and computer science. Examples include optimization, motion analysis, population modeling, and signal processing.
# Contents

## [[Limits]]
  "What happens to a function as we approach a value"
  $$\lim_{x \to a} $$
## [[Derivatives]]
The rate of change. A function which finds slope of an **original function**, $f(x)$, with respect to $x$.  

![[Tangent_line_to_a_curve.png|700]]
$$\frac{d}{dx}[x^n]$$
### [[Derivative Rules]]: 
Find derivatives without resorting to [[First Principles]]. 
- [[Constant Rule]]
  $\frac{d}{dx}(c) = 0$
  
- [[Sum Rule]]
  $\frac{d}{dx}(f(x) + g(x)) = \frac{d}{dx}(f(x)) + \frac{d}{dx}(g(x))$
  
- [[Product rule]]
  $\frac{d}{dx}(f(x) \cdot g(x)) = f'(x)g(x) + f(x)g'(x)$
  
- [[Power Rule]]
  $\frac{d}{dx}(x^n) = nx^{n-1}$
  
- [[Quotient Rule]]
  $\frac{d}{dx}\left(\frac{u(x)}{v(x)}\right) = \frac{u'(x)v(x) - u(x)v'(x)}{(v(x))^2}$
	  
- [[Chain Rule]]
  $\frac{d}{dx}(f(g(x))) = \frac{d}{dg}(f(g)) \cdot \frac{dg}{dx}$
## [[Integral]]
Adding up tiny bits. The opposite of derivatives. Finding the original function from the derivative was calculated from.
- Assuming:
	- Finding a derivative of $f(x)$ is finding $f'(x)$. 
	- Finding the integral of $f'(x)$ is finding the original $f(x)$.
	- Finding the anti derivative is finding the original $f(x)$.
- Definite
  $$\int_{a}^b$$
- Indefinite:
  $$\int$$
### [[Antiderivatives]]
  An antiderivative of a function is a function whose derivative is equal to the original function. Antiderivatives are essentially the reverse process of differentiation and are crucial in solving differential equations and evaluating integrals.
## [[Fundamental Theorem of Calculus]]
  This theorem establishes a fundamental connection between differentiation and integration. It states that if a function is continuous on a closed interval and is integrable on that interval, then the definite integral of its derivative over that interval is equal to the difference of its values at the endpoints of the interval.
- Limits at Infinity: 
  Calculus also deals with the behavior of functions as the input approaches infinity or negative infinity. This concept is crucial for understanding asymptotic behavior and determining the end behavior of functions.
- [[Continuity]]
	- Hole
	- Jump
	- Infinite
		- Asymptotes force it to diverge

## [[Infinite Sums]]
Solve differential equations, resolve logical paradoxes, computer areas, and they even appear in quantum physics.
$$
\sum_{n=1}^{\infty}
$$



## [[Continuity]]

## Problems

1. Limits
2. Derivatives
	1. [[Mia's Soccer]]
3. Integrals
	1. [[Problems - Integration]]


## [[Final Exam - Cal 1]]


# Excalidraw
To ensure drawing experience is good 
- Hide touch bar
- Hide sidebar
- Maximize screen on macbook

## [[Paul's Online Notes - Progress]]

Do these problems until you're pro

# Resources
- [Big Picture of Calculus by Eddie Woo](https://www.youtube.com/watch?v=tt2DGYOi3hc&ab_channel=EddieWoo)
- [How to think about Integration?](https://www.youtube.com/watch?v=MwVBzE7Z5gw&t=329s&ab_channel=MathTheWorld)
- [Calculus 1 Review - Intro](https://www.youtube.com/watch?v=GiCojsAWRj0&ab_channel=TheOrganicChemistryTutor)
- [Paul's Online Math Notes](https://tutorial.math.lamar.edu/Problems/CalcI/CalcI.aspx)
- [Open Stax](https://openstax.org/books/calculus-volume-1/pages/2-3-the-limit-laws)