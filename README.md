# Sudoku Solver
# Introduction
This repository demonstrates how to solve sudoku using linear [specifically integer] programs. 

The idea here is that an integer program should yield a more interpretable process than that of neural nets or more brute-force approaches like genetic algorithms. The run time for this approach may lose to faster alternatives, but a %timeit test shows solve times of 96.4 ms (with sample size 10 for a sample puzzle). Thus, any faster approaches will only be marginally quicker.

The below contents are organized as follows:
1) Repository Code: details existing files, methods, and usage
2) Technical Explanation: details logic behind the linear program setup for sudoku
3) Complete Linear Program: shows the entire linear program used

# I. Repository Code
This repository contains two python files:

1) sudoku.py 
- Contains the method to solve a sudoku puzzle
- Note that the method sudoku_solver takes on one input parameter: puzzle
- The puzzle is a 9 x 9 2D array that stores the original puzzle. Unknown cells should be populated with 0s, known cells should be populated with their respective values
- The output returns as a 9 x 9 2D array with the sudoku solution
- If there is no possible solution, the output returns a 0

2) testcases.py 
- Contains test cases to check different inputs and edge cases that may occur
- These test cases include checks for violations of each of the constraints, puzzles with unique solutions, puzzles with multiple solutions
- A lingering issue is that I am unable to return all viable solutions for puzzles with multiple solutions
- So in terms of oppotunities, I'm looking for an approach to distinguish sudokus with unique solutions from sudokus with multiple solutions


# II. Technical Explanation
The documentation below assumes familiarity with the concept of linear programs. 
If needed, an introduction can be found here: https://en.wikipedia.org/wiki/Linear_programming

### i. Decision Variables
We'll use a set of binary variables 

![formula](https://render.githubusercontent.com/render/math?math=\forall%20i%20\in%20(1,%202,%203,%20...%20,%209)%20,%20\forall%20j%20\in%20(1,%202,%203,%20...%20,%209)%20,%20\forall%20k%20\in%20(1,%202,%203,%20...%20,%209)%20:%20X_{ijk}%20\in%20(0,%201)%20)

where 

![formula](https://render.githubusercontent.com/render/math?math=i%20\in%20(1,%202,%203,%20...%20,%209)) represents the values used to play sudoku

![formula](https://render.githubusercontent.com/render/math?math=j%20\in%20(1,%202,%203,%20...%20,%209)) represents row number

![formula](https://render.githubusercontent.com/render/math?math=k%20\in%20(1,%202,%203,%20...%20,%209)) represents column number



So just to give a few examples of this notation,

![formula](https://render.githubusercontent.com/render/math?math=X_{123}%20=%201) means that the value 1 goes in the cell at row 2 column 3

![formula](https://render.githubusercontent.com/render/math?math=X_{357}%20=%200) means that the value 3 does not go in the cell at row 5 column 7

### ii. Objective Function
We can set this to be constant. Setting the objective to minimize or maximize doesn't matter.
We're simply looking for the variable arguments that satisfy all the constraints we introduce.

### iii. Constraints 
Constraint 1: Ensure that each cell is given one value 

![formula](https://render.githubusercontent.com/render/math?math=\forall%20k%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20j%20\in%20(1,%202,%203,%20...%20,%209)%20:%20\sum_{i%20=%201}^9%20{X_{ijk}}%20=%201)


Constraint 2: Ensure that each value occurs in a row once 

![formula](https://render.githubusercontent.com/render/math?math=\forall%20i%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20k%20\in%20(1,%202,%203,%20...%20,%209)%20:%20\sum_{j%20=%201}^9%20{X_{ijk}}%20=%201)


Constraint 3: Ensure that each value occurs in a column once 

![formula](https://render.githubusercontent.com/render/math?math=%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20j%20\in%20(1,%202,%203,%20...%20,%209)%20:%20\sum_{k%20=%201}^9%20{X_{ijk}}%20=%201)


Constraint 4: Ensure that each value occurs in a 3 x 3 square once 

![formula](https://render.githubusercontent.com/render/math?math=\forall%20i%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20R%20\in%20((1,%202,%203),%20(4,%205,%206),%20(7,%208,%209)),%20\forall%20C%20\in%20((1,%202,%203),%20(4,%205,%206),%20(7,%208,%209))%20:%20\sum_{j%20\in%20R}%20\sum_{k%20\in%20C}%20{X_{ijk}}%20=%201,%20)


Constraint 5: Ensure that all hints from the input are used

![formula](https://render.githubusercontent.com/render/math?math=X_{ijk}%20=%201) for all (value, row, column) combinations specified in a puzzle



# III. Complete Linear Program
Below is the reiterated format for a Sudoku LP

Maximize 0

Subject to 

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{i%20=%201}^9%20{X_{ijk}}%20=%201,%20\forall%20j%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20k%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%201}^9%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20k%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{k%20=%201}^9%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209),%20\forall%20j%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%201}^3%20\sum_{k%20=%201}^3%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%201}^3%20\sum_{k%20=%204}^6%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%201}^3%20\sum_{k%20=%207}^9%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%204}^6%20\sum_{k%20=%201}^3%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%204}^6%20\sum_{k%20=%204}^6%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%204}^6%20\sum_{k%20=%207}^9%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%207}^9%20\sum_{k%20=%201}^3%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%207}^9%20\sum_{k%20=%204}^6%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=\sum_{j%20=%207}^9%20\sum_{k%20=%207}^9%20{X_{ijk}}%20=%201,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209))

  ![formula](https://render.githubusercontent.com/render/math?math=X_{ijk}%20=%201) for specified puzzle hints

Where ![formula](https://render.githubusercontent.com/render/math?math=X_{ijk}%20\in%20(0,%201)%20,%20\forall%20i%20\in%20(1,%202,%203,%20...%20,%209)%20,%20\forall%20j%20\in%20(1,%202,%203,%20...%20,%209)%20,%20\forall%20k%20\in%20(1,%202,%203,%20...%20,%209))


