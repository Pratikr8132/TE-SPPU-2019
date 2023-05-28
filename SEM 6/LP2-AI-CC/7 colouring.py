def graph_coloring(graph, num_colors):
    num_vertices = len(graph)
    colors = [-1] * num_vertices

    if graph_coloring_util(graph, num_colors, colors, 0):
        return colors
    else:
        return None

def graph_coloring_util(graph, num_colors, colors, vertex):
    if vertex == len(graph):
        return True

    for color in range(num_colors):
        if is_valid_color(graph, colors, vertex, color):
            colors[vertex] = color

            if graph_coloring_util(graph, num_colors, colors, vertex + 1):
                return True

            colors[vertex] = -1

    return False

def is_valid_color(graph, colors, vertex, color):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and colors[i] == color:
            return False
    return True

# Example usage
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]
num_colors = 3

colors = graph_coloring(graph, num_colors)

if colors:
    print("Vertex \tColor")
    for i, color in enumerate(colors):
        print(f"{i} \t{color}")
else:
    print("No solution exists.")
































# Certainly! Let's go through the provided code and explain each line:
#
# python
# Copy code
# def graph_coloring(graph, num_colors):
#     num_vertices = len(graph)
#     colors = [-1] * num_vertices
#
#     if graph_coloring_util(graph, num_colors, colors, 0):
#         return colors
#     else:
#         return None
# The graph_coloring function is the entry point of the algorithm. It takes the graph (represented as an adjacency matrix) and the number of colors as input.
# It initializes the number of vertices in the graph and creates an array called colors to store the color assignment for each vertex. Initially, all vertices are assigned the value -1, indicating that no color has been assigned yet.
# It then calls the graph_coloring_util function to perform the actual graph coloring process. If a valid coloring is found, it returns the colors array. Otherwise, it returns None.
# python
# Copy code
# def graph_coloring_util(graph, num_colors, colors, vertex):
#     if vertex == len(graph):
#         return True
# The graph_coloring_util function is a recursive helper function used by graph_coloring to explore the search space and find a valid coloring for the graph.
# It checks if the current vertex being processed is equal to the total number of vertices in the graph. If so, it means that all vertices have been colored, and a valid coloring has been found. In this case, it returns True.
# python
# Copy code
#     for color in range(num_colors):
#         if is_valid_color(graph, colors, vertex, color):
#             colors[vertex] = color
#
#             if graph_coloring_util(graph, num_colors, colors, vertex + 1):
#                 return True
#
#             colors[vertex] = -1
# If the current vertex is not the last vertex, the function enters a loop that iterates through each color option (represented by the variable color).
# It checks if the current color option is valid for the current vertex using the is_valid_color function.
# If the color is valid, it assigns the color to the current vertex and makes a recursive call to graph_coloring_util for the next vertex (vertex + 1).
# If the recursive call returns True, indicating that a valid coloring has been found for the remaining vertices, it propagates the True result upward.
# If the recursive call returns False, it means that a valid coloring could not be achieved with the current color assignment. In this case, it backtracks by resetting the color of the current vertex to -1 and continues to the next color option.
# python
# Copy code
#     return False
# If no valid coloring is found for any color option, the function reaches the end of the loop without returning True. It then returns False to indicate that no valid coloring exists.
# python
# Copy code
# def is_valid_color(graph, colors, vertex, color):
#     for i in range(len(graph)):
#         if graph[vertex][i] == 1 and colors[i] == color:
#             return False
#     return True
# The is_valid_color function checks if assigning a particular color to the current vertex conflicts with the colors assigned to its adjacent vertices.
# It iterates through each vertex in the graph and checks if there is an edge between the current vertex and the iteration vertex (graph[vertex][i] == 1).
# If there is an edge between the vertices and the adjacent vertex has the same color as the current color option (colors[i] == color), it means there is a conflict, and the function returns False.
# If no conflicts are found, the function returns True, indicating that the current color option is valid for the vertex.
# The output of the code will be:
#
# css
# Copy code
# Vertex   Color
# 0        0
# 1        1
# 2        2
# 3        1
# This output indicates that a valid coloring has been found for the graph. Each vertex is assigned a color represented by an integer value. In this case, vertex 0 is colored with color 0, vertex 1 with color 1, vertex 2 with color 2, and vertex 3 with color 1.
#
# Now, regarding your question about Constraint Satisfaction Problem (CSP), CSP is a general problem-solving framework where the goal is to find a solution that satisfies a set of constraints. In the context of the graph coloring problem, the constraints are that no two adjacent vertices should have the same color.
#
# The given solution can be considered a CSP solution as it systematically explores the search space of color assignments for the graph vertices while respecting the constraint of adjacent vertices having different colors. It uses backtracking implicitly through the recursive calls and the branching mechanism to explore different color options.
#
# I hope this explanation clarifies the code and the concept of CSP. Let me know if you have any further questions!