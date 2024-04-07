---
tags:
  - calculus
  - integrals
---
The sum value of everything.
$$\sum\limits_{i=1}^{n} f(x_i^*) \Delta x$$
- "True" distance as n divisions approach infinityX
  
Example 1: 
- You're accelerating from 0-60 over 3 hours.
- Take speed at beginning of interval as speed for entire interval.
	- Multiply speed x time & sum.
	- Now interval it in n approximations and calculate how far you've gone.
		- 3 intervals is 60 miles: 0, 20, 40,
		- 60 intervals is 88.5 miles: $\frac{1}{20}(0 + 1 + \dots + 59)$

Example 2:

- $f(x) = \begin{cases} 1 & \text{for } 0 \leq x \leq \frac{1}{3} \\ 10 & \text{for } \frac{1}{3} \leq x \leq 1 \\\end{cases}$
- What is the average value of $f(x)$ over the interval $[0,1]$?
	- Answer: 7
	- $\frac{1}{3}(1) + \frac{2}{3}(10) = 7$


### Conclusion
Each situation was different, but we approached it in a similar way:
- take the interval,
- chop it up into pieces,
- multiply the function times the length of each piece,
- add them all up, and finally
- take a limit as the number of pieces approaches infinity.
  
In other words, we turned each problem into calculating the **limit** of a **Riemann sum.**