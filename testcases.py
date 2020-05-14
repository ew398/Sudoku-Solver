import sudoku

print("")
print("*" * 20, "Test Cases", "*" * 25)
# Violating Constraint: Each cell in a row is unique
case = [    [2, 2, 2, 2, 2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
assert sudoku.sudoku_solver(case) == 0
print("PASSED: Test Case with Repeating Cells in a Row")

# Violating Constraint: Each cell in a column is unique
case = [    [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0],
            [3, 0, 0, 0, 0, 0, 0, 0, 0]]
assert sudoku.sudoku_solver(case) == 0
print("PASSED: Test Case with Repeating Cells in a Column")

# Violating Constraint: Each cell in a 3 x 3 square is unique
case = [    [4, 4, 4, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
assert sudoku.sudoku_solver(case) == 0
print("PASSED: Test Case with Repeating Cells in a 3 x 3 Square")

# Test cases with unique solutions
case = [    [0, 0, 0, 0, 0, 9, 4, 0, 0],
            [0, 4, 0, 6, 0, 2, 0, 0, 9],
            [0, 2, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 5, 0, 6, 7, 0, 9, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 9, 0, 8, 2, 0, 5, 0, 0],
            [0, 0, 0, 0, 9, 0, 0, 3, 0],
            [4, 0, 0, 5, 0, 8, 0, 6, 0],
            [0, 0, 8, 3, 0, 0, 0, 0, 0]]
assert sudoku.sudoku_solver(case) == [ [1, 8, 3, 7, 5, 9, 4, 2, 6],
                                       [5, 4, 7, 6, 8, 2, 3, 1, 9],
                                       [9, 2, 6, 1, 3, 4, 7, 8, 5],
                                       [3, 1, 5, 4, 6, 7, 2, 9, 8],
                                       [8, 7, 2, 9, 1, 5, 6, 4, 3],
                                       [6, 9, 4, 8, 2, 3, 5, 7, 1],
                                       [7, 5, 1, 2, 9, 6, 8, 3, 4],
                                       [4, 3, 9, 5, 7, 8, 1, 6, 2],
                                       [2, 6, 8, 3, 4, 1, 9, 5, 7]]
print("PASSED: Test Case with Unique Solution")

# Test cases with multiple solutions
case = [    [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
assert sudoku.sudoku_solver(case) != 0
print("PASSED: Test Case with Multiple Solutions")

# Assessing run time
case = [    [0, 0, 0, 0, 0, 9, 4, 0, 0],
            [0, 4, 0, 6, 0, 2, 0, 0, 9],
            [0, 2, 0, 0, 3, 0, 0, 0, 0],
            [0, 0, 5, 0, 6, 7, 0, 9, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 9, 0, 8, 2, 0, 5, 0, 0],
            [0, 0, 0, 0, 9, 0, 0, 3, 0],
            [4, 0, 0, 5, 0, 8, 0, 6, 0],
            [0, 0, 8, 3, 0, 0, 0, 0, 0]]
print("\n Run time is as follows:")
%timeit sudoku.sudoku_solver(case)
