Indeterminate Forms

Derivatives are like
$\frac{0}{0}$

Integrations are like 
$0 \times \infty$

Limits of functions


## Computer Limits I
Infinite Limits

Continuous Functions
- Well behaved
- Extreme Value Theorem
	- If $f$ is continuous at every point in interval $[a,b]$ then $f$ takes on a **maximum** and **minimum** value
- Intermediate Value Theorem
	- If $f$ is continuous in $[a,b]$ for every number $z$ between $f(a)$ & $f(b)$ there is some $p$ in $[a,b]$ for which $f(p) = z$.



![[Screenshot 2024-03-18 at 1.10.37 AM.png]]


## Computing Limits II

- Rational 
	1. $$\lim_{ x \to a } \frac {x^3-a^3} {x-a}$$
	   $\frac{1}{6}$
	2. $$\lim_{ x \to 3 } \frac {x^2-x-6}{x-3}$$
	   5
- Radical 
	  1.  $$\lim_{ x \to a } \frac {\sqrt {x} - \sqrt {a}} {x-a}$$
	     $\frac {1}{2\sqrt {a}}$
	  2.  $$\lim_{ x \to \infty } (\frac {x^2}{x+1} - \frac {x^2+2}{x+3})$$
	     2
	  3.  $$\lim_{ x \to a } ( \frac {1}{x^2(x-a)} - \frac {1} {a^2(x-a)})$$
	     ![[Screenshot 2024-03-18 at 3.52.25 AM.png]]
- One Sided
	  1. $$
H(x)=\begin{cases} 
-x^2 - 2x & \text{if } x \leq -1 \\
\frac{x+2}{x} & \text{if } x > -1
\end{cases}
		$$$$\lim_{{x \to (-1)^-}} H(x) = 1 \quad \text{and} \quad \lim_{{x \to (-1)^+}} H(x) = -1$$
	  2. For what value a does not exist? $$\lim_{x \to a} \frac{|x| - |a|}{x - a}$$	![[Screenshot 2024-03-18 at 4.16.16 AM.png]]
- Absolute value

### The Squeeze Theorem
Use known limits to estimate the limits of unknown functions.

$$
\lim_{x \to c} f(x) \leq g(x) \leq h(x) \quad \text{and} \quad \lim_{x \to c} f(x) = \lim_{x \to c} h(x) = L \quad \Rightarrow \quad \lim_{x \to c} g(x) = L
$$
The centerpiece
$$
\lim_{x \to 0^+} \frac {\sin(x)}{x} = 1
$$


1. Whats the limit? Don't calculate it. Note terms $$\lim_{x \to 0} \left[5 + 2x^2 \sin\left(\frac{1}{x^7}\right)\right] = 5$$
   - $\sin$ oscilates between $1$ & $-1$ so the $x^7$ is neglible.
   - As x approaches 0 so does $2x^2$
   - The answer is 5
2. Estimate the limit $$\lim_{x \to \infty} \left( x^2 + \cos(\sin(x)) \right)$$
   - Because 
     
 ## Intermediate Value Theorum
 ![[Screenshot 2024-03-18 at 8.27.45 PM.png]]
