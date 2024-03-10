
# Optimization Problem

1. Playing soccer we're passed the ball on the sideline and want to find the best chance of scoring. 

![[Pasted Image 20240310005205_246.png]]

If we shoot from too far the goalie has a better chance of blocking it. And if we get too close then our angle of scoring becomes smaller. How do we calculate where the highest probability of scoring is?

![[application optimization.gif]]

The largest value of $\theta$ corresponds to highest probability of scoring

## Maximizing with differentiate


![[optimization-1.png]]

- $\theta$ depends on x
- We want the relationship between x & $\theta$

![[optimization-2.png]]

We're going from opposite to adjacent
Remember these rules:

![[Screenshot 2024-03-09 at 10.13.01 PM.png]]


$\theta_{1} + \theta_{2}$ is sorta what we're looking for, but the difference.
![[optimization-3.png]]

How can we formulate the differential equation?
![[Screenshot 2024-03-10 at 1.36.37 AM.png]]


So we're left with: 
$tan^{-1} \frac {wx}{x^2+(w+b)b}$

Compute this we can find the max
$0(x) = tan^{-1} \frac {wx}{x^2+(w+b)b}$  

We have to find the critical points


How to find the relationship?

Exporting image respects background color