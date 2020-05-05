# Sudoku Solver
This repository demonstrates how to solve sudoku using linear [specifically integer] programs. 
The idea here is that an integer program should yield a more interpretable process than that of neural nets or more brute-force approaches like genetic algorithms.

The documentation below acts on the assumption that the reader is familiar with the concept of linear programs.
In the space below, I'll elaborate on decision variables used, objective functions to pursue, and associated constraints.



Decision Variables:
We'll create a binary variable $X_{ijk}$ to show if integer i occurs in row j and column k of a given sudoku.


Constraint 1
![equation](https://latex.codecogs.com/png.latex?%5Clarge%20%5Csum%5Climits_%7Bi%20%3D%201%7D%5E9%20%7BX_%7Bijk%7D%7D%20%3D%201%3A%5Cforall%20j%20%5Cin%20%281%2C%202%2C%20...%2C%209%29%2C%20k%20%5Cin%20%281%2C%202%2C%20...%2C%209%29)

Constraint 2

Constraint 3w

Constraint 4

Constraint 5
