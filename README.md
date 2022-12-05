# Numerical_Solver

## Objective

The aim of this project is to compare and analyze the behavior of the different numerical methods used for solving system of linear equations:
  1. Gauss Elimination
  2. Gauss Jordan
  3. LU Decomposition
  4. Gauss Seidel
  5. Jacobi Iteration

## Description
Application to solve a linear system of equation which takes input the system of linear equations, the method to use and its required parameters if exists for this method.

## Specification

implemented interactive GUI application that does the following:
  1. Accepts an inputfora system of linearequations:
    a. The equations can be of any format.
    b. The input validation should be bullet-proof.
    c. Number of variables must equal the number of equations.
    d. Coefficients must be numbers (0 or non-existing is allowed).

  2. Chooseany of the previously mentioned methodsto solve the given equation via a drop-down list.

  3. Parameters -if it applicable for the chosen solving method.

  4. Input for specifing the required precision. (If user chooses not to provide it, a default value is applied)
  
  5. Solve button to display the output if exists with displaying the run time.

  6. Selecting the prefered pivoting method if wanted.
