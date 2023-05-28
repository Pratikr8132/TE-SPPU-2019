n = int(input("Enter No. of Nodes: "))
graph = [[0 for i in range(n)] for j in range(n)]

while (ch := input("Enter Edges (N to stop): ")) != 'N':
    x, y = map(int, ch.split())
    graph[x][y] = graph[y][x] = 1

method = input("Choose search method (BFS or DFS): ")

if method.upper() == "BFS":
    print("BFS ====>")
    queue = []
    visited = [0 for i in range(n)]

    def bfs(node):
        visited[queue.pop(0)] = 1
        print(node)
        for i in range(n):
            if graph[node][i] == 1 and not visited[i] and i not in queue:
                queue.append(i)
        if not queue:
            return
        bfs(queue[0])

    queue.append(0)
    bfs(queue[0])

elif method.upper() == "DFS":
    print("DFS ====>")
    stack = []
    visited = [0 for i in range(n)]

    def dfs(node, stack):
        print("visited ===> ", node)
        visited[stack.pop(0)] = 1

        s = []
        for i in range(n):
            if graph[node][i] == 1 and not visited[i] and i not in stack:
                s.append(i)

        stack = s + stack
        if not stack:
            return

        dfs(stack[0], stack)

    stack.append(0)
    dfs(stack[0], stack)

else:
    print("Invalid search method. Please choose either 'BFS' or 'DFS'.")



































#
#
#
#
#
# EXPLAIN ME IN DEPTH EVERYTHING FROM DEFINITION TO ALGORITHM AND USES
#
# ChatGPT
# Certainly! Let's dive into the details of BFS (Breadth-First Search) and DFS (Depth-First Search), including their definitions, algorithms, and use cases.
#
# Definition:
#
# Breadth-First Search (BFS): It is an algorithm used for traversing or searching graph or tree data structures. It explores all the vertices of a graph or nodes of a tree in breadth-first order, visiting all the vertices at the same level before moving to the next level.
#
# Depth-First Search (DFS): It is also an algorithm used for traversing or searching graph or tree data structures. It explores all the vertices of a graph or nodes of a tree in depth-first order, visiting a vertex and its adjacent vertices recursively before backtracking.
#
# BFS Algorithm:
#
# BFS follows a queue-based approach to traverse a graph or tree in a breadth-first manner. Here's a step-by-step breakdown of the BFS algorithm:
#
# Choose a starting vertex and enqueue it into a queue.
# Mark the starting vertex as visited.
# While the queue is not empty:
# Dequeue a vertex from the queue.
# Visit the dequeued vertex and process it.
# Enqueue all the unvisited adjacent vertices of the dequeued vertex.
# Mark the dequeued vertex as visited.
# If there are no more vertices in the queue, the BFS traversal is complete.
# The BFS algorithm guarantees that it visits all the vertices at distance k from the starting vertex before moving to vertices at distance k+1.
#
# DFS Algorithm:
#
# DFS follows a stack-based approach or recursion to traverse a graph or tree in a depth-first manner. Here's a step-by-step breakdown of the DFS algorithm:
#
# Choose a starting vertex and push it onto a stack or pass it to the recursive function.
# Mark the starting vertex as visited.
# While the stack is not empty:
# Pop a vertex from the stack or use the passed vertex in the recursive function.
# Visit the popped vertex and process it.
# Push all the unvisited adjacent vertices of the popped vertex onto the stack or pass them to the recursive function.
# Mark the popped vertex as visited.
# If there are no more vertices in the stack, the DFS traversal is complete.
# The DFS algorithm explores as far as possible along each branch before backtracking.
#
# Uses of BFS and DFS:
#
# BFS is primarily used for finding the shortest path or the minimum number of edges between two nodes in an unweighted graph. It can also be used to solve various graph problems like finding connected components, checking bipartiteness, and solving puzzles like the 8-puzzle or maze-solving.
#
# DFS is commonly used to explore or traverse a graph or tree. It is useful for problems that involve finding paths, detecting cycles, topological sorting, solving puzzles like the N-Queens problem or Sudoku, and generating spanning trees.
#
# Both BFS and DFS have their own advantages and use cases. BFS guarantees the shortest path in an unweighted graph, while DFS is often simpler to implement recursively and can provide more information about the structure of a graph or tree.
#
# It's important to choose the appropriate algorithm based on the problem requirements and the characteristics of the graph or tree being traversed.

# -------------> CODE EXPLANATION
# Certainly! Let's go through the code step by step and explain its functionality:
#
# python
# Copy code
# n = int(input("Enter No. of Nodes: "))
# graph = [[0 for i in range(n)] for j in range(n)]
# In this part, the code prompts the user to enter the number of nodes in the graph and initializes an adjacency matrix called graph with n nodes, represented as a 2D list.
#
# python
# Copy code
# while (ch := input("Enter Edges (N to stop): ")) != 'N':
#     x, y = map(int, ch.split())
#     graph[x][y] = graph[y][x] = 1
# This section takes input from the user to define the edges of the graph. The user enters the node pairs that are connected by an edge. The input stops when the user enters 'N'. The code then updates the adjacency matrix graph by setting the corresponding values to 1 to indicate the existence of an edge between the nodes.
#
# python
# Copy code
# method = input("Choose search method (BFS or DFS): ")
# Here, the user is prompted to choose the search method between BFS and DFS.
#
# python
# Copy code
# if method.upper() == "BFS":
#     print("BFS ====>")
#     queue = []
#     visited = [0 for i in range(n)]
#
#     def bfs(node):
#         visited[queue.pop(0)] = 1
#         print(node)
#         for i in range(n):
#             if graph[node][i] == 1 and not visited[i] and i not in queue:
#                 queue.append(i)
#         if not queue:
#             return
#         bfs(queue[0])
#
#     queue.append(0)
#     bfs(queue[0])
# If the chosen method is BFS, the code enters this block. It initializes a queue, a visited array, and defines the BFS function. The BFS function follows the previously explained BFS algorithm. It starts from a given node, visits it, enqueues its unvisited neighbors, and continues until the queue is empty. The BFS traversal order is printed as the nodes are visited.
#
# python
# Copy code
# elif method.upper() == "DFS":
#     print("DFS ====>")
#     stack = []
#     visited = [0 for i in range(n)]
#
#     def dfs(node, stack):
#         print("visited ===> ", node)
#         visited[stack.pop(0)] = 1
#
#         s = []
#         for i in range(n):
#             if graph[node][i] == 1 and not visited[i] and i not in stack:
#                 s.append(i)
#
#         stack = s + stack
#         if not stack:
#             return
#
#         dfs(stack[0], stack)
#
#     stack.append(0)
#     dfs(stack[0], stack)
# If the chosen method is DFS, the code enters this block. It initializes a stack, a visited array, and defines the DFS function. The DFS function follows the previously explained DFS algorithm. It starts from a given node, visits it, pushes its unvisited neighbors onto the stack, and continues until the stack is empty. The DFS traversal order is printed as the nodes are visited.
#
# python
# Copy code
# else:
#     print("Invalid search method. Please choose either 'BFS' or 'DFS'.")
# If an invalid search method is entered, the code prints an error message.
#
# The combined code allows the user to input the graph structure and choose between BFS and DFS for traversal. The respective traversal order is then printed based on the chosen method.

#
# Sample Input 1:
#
# Enter No. of Nodes: 5
# Enter Edges (N to stop): 0 1
# Enter Edges (N to stop): 0 2
# Enter Edges (N to stop): 1 3
# Enter Edges (N to stop): 1 4
# Enter Edges (N to stop): N
# Choose search method (BFS or DFS): BFS
#
# Enter No. of Nodes: 6
# Enter Edges (N to stop): 0 1
# Enter Edges (N to stop): 0 2
# Enter Edges (N to stop): 1 3
# Enter Edges (N to stop): 2 4
# Enter Edges (N to stop): 2 5
# Enter Edges (N to stop): N
# Choose search method (BFS or DFS): DFS