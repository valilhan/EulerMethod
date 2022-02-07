# EulerMethod
# Differential Equation

## Find Exact

Find exact solution:

First order nonlinear ordinary differential equation

Let's do substitution , than , ,
The equation becomes:

**→**
Convert equation into separable form:
→
Integrate both part
→ →
Substitute back to original equation
→ →
Solve IVP: if and than →
Exact solution:

## UML - diagram of class

### ⎩

### ⎨

⎧y′=( 1 +xy)ln((x+xy))+xy
y( 1 )= 2
x∈( 1 , 6 )
x= 0

```
z= 1 + xy z′= y′xx+ 2 x′y y=xz−x y′= x^2 z′+xxz−x
```
```
x^2 z′+xxz−x =zln(z)+z− 1 z′x=zln(z)
```
```
ddxzx=zln(z) zdlnzz = dxx
```
∫ zdlnzz =∫ dxx ln(ln(z))=ln(x)+ln(c) ln(z)=xc

ln( 1 +xy)=xc 1 +xy =exc y=(exc− 1 )x
x= 1 y= 2 2 =ec− 1 c=ln( 3 )
y=(exln(^3 )− 1 )x


The main class of the source code consists of four classes: MyFunction, GRID,
NumMethod, MyExactSolution and ImprovedEulerMethod, RungeKuttaMethod,
EulerMethod. Classes NumMethod and MyExactSolution use the class Function in their
implementation, while class NumMethod extend the class Solutions and Solutions
extends Grid. The class MyFunction contains the given differential equation. The class
Grid contains the step, points of the x axes and y points for all numerical methods and
exact solution. The class MyExactSolution finds y values for all methods. The class


NumMethod finds all types of errors and the dependence of errors on the number of grid
cells.



There is the first tab of the application below. It shows the graph of exact and numerical


solutions, the graph of local truncation errors for numerical solutions and the graph of
global
truncation errors for numerical solutions. It is possible to hide solutions on the plots.
Values x0,
y0, X and N can be changed.
From this graphs we can see that the best approximation gives the Runge-Kutta
method.

There is the second tab of the application below. It shows the dependence of errors
from the
number of grid cells for local and global truncation errors. It is possible to hide lines on
graphs.
Values n0 and N can be changed. Values x0, y0, X and N are taken from the first tab.
From these graphs one can notice that the more the number of grid cells, the less the
error



