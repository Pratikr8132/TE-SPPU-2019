def isSafe(arr, x, y, n):
    for row in range(x):
        if arr[row][y] == 1:
            return False
    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1

    return True


def nQueen(arr, x, n):
    if x >= n:
        return True

    for col in range(n):
        if isSafe(arr, x, col, n):
            arr[x][col] = 1
            if nQueen(arr, x+1, n):
                return True
            arr[x][col] = 0

    return False


if __name__ == "__main__":
    n = int(input("Enter n: "))
    arr = [[0 for j in range(n)] for i in range(n)]
    if nQueen(arr, 0, n):
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=' ')
            print()





















#
#
#
#
#
#
# Sure! Let's go through the code line by line and explain its functionality:
#
# The isSafe function checks if it is safe to place a queen at position (x, y) on the chessboard. It takes the chessboard arr, current row x, current column y, and board size n as parameters.
#
# The function uses three nested loops to check for conflicts with previously placed queens:
#
# The first loop iterates through all rows above the current row. If a queen is found in the same column (arr[row][y] == 1), it means there is a conflict, and the function returns False.
# The second and third loops check for conflicts along the diagonals. They move diagonally up-left and up-right from the current position (x, y) and check if there is a queen present in any of those positions. If a queen is found, it means there is a conflict, and the function returns False.
# If no conflicts are found, the function returns True, indicating that it is safe to place a queen at position (x, y).
#
# The nQueen function solves the N-Queens problem using backtracking. It takes the chessboard arr, current row x, and board size n as parameters.
#
# If the current row x is equal to or exceeds the board size n, it means all queens have been successfully placed, and the function returns True.
#
# The function uses a loop to iterate through each column in the current row. It checks if it is safe to place a queen in that column using the isSafe function. If it is safe, it marks that position as a queen (arr[x][col] = 1) and recursively calls nQueen for the next row (x+1).
#
# If the recursive call to nQueen returns True, it means a solution has been found, and the function returns True.
#
# If the recursive call does not result in a solution, it backtracks by resetting the current position to empty (arr[x][col] = 0).
#
# If all columns have been explored in the current row without finding a solution, the function returns False.
#
# In the main part of the code, the user is prompted to enter the board size n.
#
# A 2D list arr is created to represent the chessboard, initially filled with zeros.
#
# The nQueen function is called with the initial row as 0.
#
# If a solution is found (nQueen returns True), the chessboard is printed by iterating through each position and displaying the value (0 or 1).
#
# Now, regarding the N-Queens problem:
# The N-Queens problem is a classic problem in computer science and combinatorial optimization. The objective is to place N queens on an N×N chessboard in such a way that no two queens threaten each other. In other words, no two queens should share the same row, column, or diagonal.
#
# Here are some potential questions and answers related to the N-Queens problem:
#
# Q: What is the goal of the N-Queens problem?
# A: The goal is to find a placement of N queens on an N×N chessboard such that no two queens threaten each other.
#
# Q: How many solutions are there for the N-Queens problem?
# A: The number of solutions depends on the size of the chessboard. For smaller board sizes (e.g., N = 4, 5, 6), there are multiple solutions. However, for larger board sizes, the number of solutions grows exponentially, and finding all solutions becomes computationally intensive.
#
# Q: What is backtracking, and how is it used in the N-Queens problem?
# A: Backtracking is a technique used to systematically explore all possible solutions by incrementally building a solution and undoing choices that lead to invalid solutions. In the N-Queens problem, backtracking is employed to place queens on the board while ensuring they do not threaten each other. If a queen placement leads to a conflict, the algorithm backtracks and tries another position.
#
# Q: Are there any alternative approaches to solving the N-Queens problem?
# A: Yes, there are alternative approaches to solving the N-Queens problem, such as using different data structures, heuristics, or constraint satisfaction algorithms like Constraint Programming (CP) or Genetic Algorithms (GA). These approaches may provide more efficient or optimized solutions depending on the problem size and constraints.
#
# Q: Can the N-Queens problem be solved for any value of N?
# A: The N-Queens problem can be solved for any positive integer N. However, as N increases, the problem becomes more complex and computationally intensive. Finding solutions for large N values can be challenging and may require optimized algorithms or parallel computing techniques.
#
# Feel free to ask if you have any more specific questions or need further clarification!
#
#
#
#
#
# User
# what is csp
# ChatGPT
# CSP stands for Constraint Satisfaction Problem. It is a mathematical problem defined as a set of objects whose state must satisfy a number of constraints or limitations. CSPs are widely used in artificial intelligence, operations research, and computer science.
#
# In a CSP, the problem is typically defined in terms of variables, domains, and constraints:
#
# Variables: These represent the objects or entities that we need to assign values to. Each variable has a set of possible values called its domain.
#
# Domains: A domain represents the set of values that a variable can take. The values in the domain must satisfy any constraints imposed by the problem.
#
# Constraints: These define the limitations or conditions that the variables and their assigned values must adhere to. Constraints restrict the combinations of values that are considered valid or feasible.
#
# The goal of a CSP is to find a valid assignment of values to the variables that satisfies all the constraints. The assignment must satisfy all constraints simultaneously, without violating any of them.
#
# CSPs are widely used in various problem domains, such as scheduling, planning, resource allocation, graph coloring, Sudoku, and the N-Queens problem. The techniques used to solve CSPs include backtracking, constraint propagation, local search, and intelligent search heuristics.
#
# CSPs provide a formal framework for representing and solving problems that involve constraints and discrete decision variables. They are a powerful tool for modeling and solving real-world problems that involve complex constraints and decision-making