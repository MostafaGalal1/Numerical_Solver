# Numerical Solver

## Objective

The aim of this project is to compare and analyze the behavior of the different numerical methods used for solving system of linear equations:
  1. Gauss Elimination
  2. Gauss Jordan
  3. LU Decomposition
  4. Gauss Seidel
  5. Jacobi Iteration

## Description
Application to solve a linear system of equations which takes input the system of linear equations, the method to use and its required parameters if exists for this method.

## Specification

Implemented interactive GUI application that does the following:
  1. Accepts an input for a system of linear equations:
     * The equations can be of any format.
     * Bullet-proof input validation.
     * Number of variables must equal the number of equations.
     * Coefficients must be numbers (0 or non-existing is allowed).
    
  2. Choose any of the previously mentioned methods to solve the given system via a drop-down list.

  3. Parameters -if it applicable for the chosen solving method.

  4. Input for specifing the required precision. (If user chooses not to provide it, a default value is applied)

  5. Solve button to display the output if exists with displaying the run time.

  6. Selecting the prefered pivoting method if wanted.

The following table summarizes the required methods and their input parameters:
| Method | Input | Parameters |
|------|----------|--------|
| Gauss Elimination | System of Linear Equations | None |
| Gauss-Jordan | System of Linear Equations | None |
| LU Decomposition | System of Linear Equations | Drop-down list for the format of L & U: <ol><li>Downlittle Form</li><li>Crout Form</li><li>Cholesky Form</li></ol> |
| Gauss-Seidel | System of Linear Equations | <ol><li>Initial Guess</li><li>Stopping Condition: <ul><li>Number of Iterations</li><li>Absolute Relative Error</li></ul></ol> |
| Jacobi-Iteration | System of Linear Equations | <ol><li>Initial Guess</li><li>Stopping Condition: <ul><li>Number of Iterations</li><li>Absolute Relative Error</li></ul></ol> |
