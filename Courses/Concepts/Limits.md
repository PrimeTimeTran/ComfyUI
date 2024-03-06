The limit as x approaches 0
$$\lim_{x \to 0} $$
#### How to evaluate a limit?
- Analytically:
	- First Principles
		- $f(x)=\frac{lim} {x\to2}\frac{x^2-2}{x-2}$
	- Secants
		- Lines which cross a line at two points.
		- We select a few close to the tangent to get an close approximation to the value we're looking for, `m` at point `x`.
	- Tangent
		- A single point on a graph
		- Finding the slope at this point was the problem which gave birth to limits
- Graphically

#### Methods Analytically

1. Plugin: 
	1. First principles is plugging in values(secants) and observing behavior of their gradients as they approach the limit.
		- Clearly, `f(2)` won't work. It's dividing by 0.
		- But we can plug in 2.1, 2.01, 2.001, 2.0001 and so forth
		  $$\lim_{x\to_{2}} \ \frac{x^2-4}{x-2}$$
2. Factoring:
	- If we have a fraction we should factor
	- Difference of cubes
	  $$\lim_{x\to3} \ \, \frac{x^3-27}{x-3}$$
3. Complex fraction:
	- Multiply top & bottom by common denominator of top's fractions.
	- If complex fraction then multiply top & bottom by common denominator of the numerator
	  $$\lim_{x\to3} \ \, \frac{{\frac{1}{x}-\frac{1}{3}}{}}{x-3}$$
	  > Here: `3x` 
4. Square root
	- Multiply top & bottom by the  conjugate of the expression that has the square root
		$$\lim_{x\to_{9}} \ \, \frac{\sqrt{x}-3}{x-9}$$
		> Here: $\sqrt{x}+3$
		> Eventually you'll reach a point where you can plug in a value though
		> 
5. Complex fraction with radicals:
  $$\lim_{x\to4} \ \, \frac{\frac{1}{\sqrt{x}}-\frac{1}{2}}{x-4}$$
	- Multiple top & bottom by numerator's common denominators but conjugate:
	- First common denominator then conjugate

If fraction with a sqrt then multiply top & bottom by conjugate of the sqrt factor


Graphically
- If left & right side approaches are not the same then the limit does not exist