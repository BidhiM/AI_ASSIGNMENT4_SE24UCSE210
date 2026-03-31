
##  Overview
This project demonstrates the implementation of classic **Constraint Satisfaction Problems (CSP)** using Python. It includes:
1. Map Coloring (Australia)
2. Map Coloring (Telangana Districts)
3. Sudoku Solver
4. Crypt-Arithmetic Puzzle Solver

Each problem is solved using **Backtracking with constraints**, ensuring valid and optimized solutions.

###  Map Coloring – Australia
* Colors the 7 regions: WA, NT, QLD, SA, NSW, V, T
* Constraint: No adjacent regions share the same color
* Technique: Backtracking CSP

###  Map Coloring – Telangana (33 Districts)
* Colors all 33 districts of Telangana
* Uses a realistic adjacency graph
* Constraint: Neighboring districts must have different colors
* Output: Visual colored map

###  Sudoku Solver
* Solves a standard 9×9 Sudoku grid
* Empty cells represented by `0`
* Constraints:
  * Unique numbers in each row
  * Unique numbers in each column
  * Unique numbers in each 3×3 subgrid

###  Crypt-Arithmetic Puzzle
* Solves:
  **SEND + MORE = MONEY**
* Constraints:
  * Each letter maps to a unique digit
  * No leading zeros
  * Arithmetic equation must be satisfied
Solution:
9567 + 1085 = 10652


##  Technologies Used
* Python 3
* Libraries:
  * matplotlib (for visualization)
  * plotly / geopandas (optional for real maps)

##  Concepts Covered
* Constraint Satisfaction Problems (CSP)
* Backtracking Algorithm
* Constraint Propagation
* Graph Coloring
* Combinatorial Search

