# Sudoku Solver
## Introduction
This repository demonstrates how to solve sudoku using linear [specifically integer] programs. 

The idea here is that an integer program should yield a more interpretable process than that of neural nets or more brute-force approaches like genetic algorithms. The run time for this approach may lose to faster alternatives, but a %timeit test shows solve times of 96.4 ms (with sample size 10 for a sample puzzle). Thus, any faster approaches will only be marginally quicker.

Keep in mind this result could be anecdotal, so take these sample findings with a grain of salt. 

# Technical Details
The documentation below assumes familiarity with the concept of linear programs. 
If needed, an introduction can be found here: https://en.wikipedia.org/wiki/Linear_programming

## I. Decision Variables
We'll use a set of binary variables ![formula](https://render.githubusercontent.com/render/math?math=X_{ijk}%20\in%20(0,%201)%20,%20\forall%20i%20\in%20(1,%202,%203,%20...,%209)%20,%20\forall%20j%20\in%20(1,%202,%203,%20...,%209)%20,%20\forall%20k%20\in%20(1,%202,%203,%20...,%209))

where ![formula](https://render.githubusercontent.com/render/math?math=i%20\in%20(1,%202,%203,%20...,%209)) represents the values 1 through 9 that a specified cell can take

and ![formula](https://render.githubusercontent.com/render/math?math=j%20\in%20(1,%202,%203,%20...,%209)) represents row number

and ![formula](https://render.githubusercontent.com/render/math?math=k%20\in%20(1,%202,%203,%20...,%209)) represents column number

So just to give a few examples of this notation,

![formula](https://render.githubusercontent.com/render/math?math=X_{123}%20=%201) means that the value 1 goes in the cell at row 2 column 3

![formula](https://render.githubusercontent.com/render/math?math=X_{357}%20=%200) means that the value 3 does not go in the cell at row 5 column 7

## II. Objective Function
We can set this to be constant, since we're simply concerned with having all constraints satisfied.

## III. Constraints 
Constraint 1: Ensure that each cell is given one value 
$\sum\limits_{i = 1}^9 {X_{ijk}} = 1:\forall j \in (1, 2, ..., 9), k \in (1, 2, ..., 9)$

Constraint 2: Ensure that each value occurs in a row once 
$\sum\limits_{j = 1}^9 {X_{ijk}} = 1:\forall i \in (1, 2, ..., 9), k \in (1, 2, ..., 9)$

Constraint 3: Ensure that each value occurs in a column once 
$\sum\limits_{k = 1}^9 {X_{ijk}} = 1:\forall i \in (1, 2, ..., 9), j \in (1, 2, ..., 9)$

Constraint 4: Ensure that each value occurs in a 3 x 3 square once 
$\sum\limits_{j = 1}^3 \sum\limits_{k = 1}^3 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 1}^3 \sum\limits_{k = 4}^6 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 1}^3 \sum\limits_{k = 7}^9 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 4}^6 \sum\limits_{k = 1}^3 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 4}^6 \sum\limits_{k = 4}^6 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 4}^6 \sum\limits_{k = 7}^9 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 7}^9 \sum\limits_{k = 1}^3 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 7}^9 \sum\limits_{k = 4}^6 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$
$\sum\limits_{j = 7}^9 \sum\limits_{k = 7}^9 {X_{ijk}} = 1: \forall i \in (1, 2, ..., 9)$

Constraint 5: Ensure that all hints from the input are used
$X_{ijk} = 1$ for all numbers specified in hints
