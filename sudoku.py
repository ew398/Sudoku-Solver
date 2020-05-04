import pulp

def sudoku_solver(puzzle):
    """
    Precondition:
        Input: Sudoku puzzle written as 2D array. All unknown cells are listed as 0s
        Returns: Corresponding puzzle solution
    """

    # Common ranges to iterate on
    nums = range(1, 10)
    nums2 = [range(1, 4), range(4, 7), range(7, 10)]

    # Create linear program
    problem = pulp.LpProblem('Problem', pulp.LpMaximize) # Create maximization program
    x = pulp.LpVariable.dicts('x', [(val, row, col) for val in nums for row in nums for col in nums], cat = 'Binary') # Create variables
    problem += 0 # Create objective function

    # Constraint 1: Make sure each cell has one value
    for row in nums:
        for col in nums:
            problem += (pulp.lpSum([x[(val, row, col)] for val in nums]) == 1)

    # Constraint 2: Make sure each cell in a row has a different value
    for val in nums:
        for col in nums:
            problem += (pulp.lpSum([x[(val, row, col)] for row in nums]) == 1)

    # Constraint 3: Make sure each cell in a column has a different value
    for val in nums:
        for row in nums:
            problem += (pulp.lpSum([x[(val, row, col)] for col in nums]) == 1)

    # Constraint 4: Ensure each cell in a 3 x 3 square has a different value
    for val in nums:
        for row3 in nums2:
            for col3 in nums2:
                problem += (pulp.lpSum([x[(val, row, col)] for row in row3 for col in col3]) == 1)

    # Constraint 5: Ensure additional constraints from specific puzzle are met
    for row in nums:
        for col in nums:
            if puzzle[row - 1][col - 1] != 0:
                problem += (x[(puzzle[row - 1][col - 1], row, col)] == 1)

    # Solve Linear program
    problem.solve()
    if problem.solve() != 1:
        return Null
    else:
      solution = []
      for row in nums:
          for col in nums:
              for val in nums:
                  if x[(val, row, col)].varValue == 1:
                      solution.append(val)
      output = [0] * 9
      for i in range(9):
        output[i] = solution[9 * i : 9 * (i + 1)]
      return output
