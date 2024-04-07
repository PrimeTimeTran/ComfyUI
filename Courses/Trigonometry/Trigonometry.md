# Trig Overview

1. The six trigometric functions:
	- Sine, Cosine, Tangent, Cosecant, Secant, Cotangent
		- Abbreviated: 
			- sin, cos, tan, csc, sec, cot
	- SOH, CAH, TOA
		- Sine: Opposite/Hypotenuse
		- Cosine: Adjacent/Hypotenuse
		- Tangent: Opposite/Adjacent
	- Reciprocals
		- Sine -> Cosecant: Hyp/Opp
		- Cosine -> Secant: Hyp/Adj 
		- Tangent -> Cotangent: Adjacent/Opposite
	- Trig functions are properties of angles, not triangles.
	- Trig functions are unitless.
	- Written and read as sin $\theta$ not sin $(\theta)$
2. Cartesian Coordinates and Quandrants
	- I, II, III, IV
	- (+,+), (-, +), (-, -), (+, -)
3. Angle Measurements in Degrees and Radians
	- 0º - 360º
	- Quarters are 90º
	- 45º split each quandrant
	- Circumference = 2πr
	- 360º = 2πr radians
	- 180º = π radians
	  ![[Screenshot 2024-03-26 at 6.01.00 AM.png | 500]]
4. The Pythagorean Theorem
	- $a^2+b^2 = c^2$
5. The Unit Circle
    - Large, Medium, Small:
        - Large: $\frac {\sqrt {3}}{2}$
        - Medium: $\frac {\sqrt {2}}{2}$
        - Small: $\frac {1}{2}$



## Conversions

### Pi to Radians
- $\pi$ to degrees: 
	- Multiply by $\frac {180^{{\degree}}}{\pi}$

Find the angle measurement in degrees that is equivalent to $\frac {7\pi}{6}$ radians.
### Convert from radians to degrees
To convert from radians to degrees we use:

$$\frac {180^{\degree}}{\pi}$$
Multiply it by the problem you're given.
$$
 \frac {7\pi}{6} \times \frac {180^{\degree}}{\pi} = \frac {1260\pi^{\degree}}{6\pi} = \frac {1260^{\degree}}{6} = 210^{\degree}
$$
### Degrees to radians
To solve for $270^{\degree}$ we use:
$$\frac {\pi}{180^{\degree}}$$
Multiply times the problem given
$$
270^{\degree} \times \frac {\pi}{180^{\degree}} = \frac {3}{2}radians
$$
### Convert from degree to angle
To solve for something bigger than 360

1. Find the angle in radians that is coterminal with $795^{\degree}$
   
	- Subtract 360 until it's between 0 & 360
	- Multiply by 2 + degree/360 we want
	- Convert from degree to radians by multiplying by 
		  $\frac {\pi}{180^{\degree}}$
	- Result is $\frac {5\pi}{12}$

### Convert from ratio to degree
- arctan
- arcsine
- arccosine
  
## Laws of Trig Functions
### Law of Cosines
- Need 2 side lengths
- Find 3rd side length.
- Find interior angles of non right triangles.
- Formula is different
	- Obtuse: $c^2 > a^2 + b^2$
	- Acute: $c^2 < a^2 + b^2$
![[Screenshot 2024-04-03 at 4.39.30 PM.png]]
- With 2 sides & angle find last side:
- With 3 sides find angles:
![[Screenshot 2024-04-04 at 1.16.24 PM.png | 500]]
### Law of Sines
- A triangle's side lengths are proportional to the sines of their opposite angles. We call this fact the **law of sines**.
- Need 1 side length, 2 angles.
- Side lengths are proportional to the sines of their opposite angles:
  ![[Screenshot 2024-04-04 at 1.55.10 PM.png | 400]]
### Ambiguous Cases

- Acute vs obtuse.
  ![[Screenshot 2024-04-04 at 2.41.34 PM.png|300]]
- Unit circle where quadrant 2 & 1. Their sin's can match
	- Quad 2: ![[Screenshot 2024-04-04 at 2.43.06 PM.png | 300]]
	- Quad 1: ![[Screenshot 2024-04-04 at 2.43.40 PM.png | 300]]
- Rules to check if triangle possible.
  ![[Screenshot 2024-04-04 at 2.49.59 PM.png | 400]]
## Transformations
- We can stretch horizontally & vertically
- Transform:
	- Amplitude
	- Period
	- Frequency
	- Phase Shift
	- Midline

![[Screenshot 2024-04-04 at 3.15.46 PM.png | 500]]

### Graphed Trig Functions
![[Screenshot 2024-04-05 at 6.06.22 PM.png]]
- Reciprocals:
	- $\sin(θ) = 0$
		- $csc(θ) = 1/sin(θ)$
	- $\cos(θ) = 1$
		- $\sec(θ) = 1/\cos(θ)$
	- $\tan(θ) = 0$
		- $\cot(θ) = 1/\tan(θ)$
- Transform one graph into another:
	- Phase Shifts: Shifting the right amount can turn one into another
		- $\sin(θ) = \cos\left( θ - \frac{π}{2} \right)$
		- $\cos(θ) = \sin\left( θ + \frac{π}{2} \right)$
	- Reflections
- Transform reciprocals into one another
	- $\csc(θ) = \sec(θ - \frac{π}{2})$
	- $\sec(θ) = \csc(θ + \frac{π}{2})$
- Even-Odd Identities:
	- Even functions
		- Outputs of a & -a always have the same output
		- They output the same y value
	- Odd functions:
		- Outputs of a and -a have outputs of the same magnitude but with opposite signs
		- Rotate 180º or π radians to make the same
	- $\sin(θ)$ is odd
		- $\sin(-θ) = -\sin(θ)$
	- $\cos(θ)$ is even
		- $\cos(-θ) = \cos(θ)$
	- $\tan(θ)$ is odd
		- $\tan(-θ) = -\tan(θ)$