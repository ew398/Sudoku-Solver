import pulp


def sudoku_solver(puzzle):
    """
    Precondition:
        Input:
            - Sudoku puzzle written as 2D array
            - All unknown elements in sudoku puzzle are populated with 0s
            - All known elements in sudoku puzzle are populated with their corresponding value
        Returns:
            - Solution array to the input array
            - If there is no solution, 0 will be returned
            - If there is a unique solution, the corresponding 2D solution array will be shown
            - If there multiple solutions, the first 2D array solution that the linear program comes across will be shown
    """

    # Common ranges to iterate on
    nums = range(1, 10)

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
    nums2 = [range(3 * x + 1, 3 * x + 4) for x in range(3)]
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
        return 0
    else:
        # Initialize sudoku solution in 2D array
        solution = [int(val * x[(val, row, col)].varValue) for row in nums for col in nums for val in nums if x[(val, row, col)].varValue > 0]
        solution2 = np.array(solution)
        return np.reshape(solution2, (9, 9))
