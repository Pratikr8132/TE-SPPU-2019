def graph_coloring(graph, num_colors):
    vertices = list(graph.keys())
    colors = {vertex: -1 for vertex in vertices}

    if graph_coloring_util(graph, num_colors, colors, 0, vertices):
        return colors
    else:
        return None

def graph_coloring_util(graph, num_colors, colors, vertex, vertices):
    if vertex == len(vertices):
        return True

    current_vertex = vertices[vertex]

    for color in range(num_colors):
        if is_valid_color(graph, colors, current_vertex, color):
            colors[current_vertex] = color

            if graph_coloring_util(graph, num_colors, colors, vertex + 1, vertices):
                return True

            colors[current_vertex] = -1

    return False

def is_valid_color(graph, colors, vertex, color):
    for adjacent_vertex in graph[vertex]:
        if colors[adjacent_vertex] == color:
            return False
    return True

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
num_colors = 3

colors = graph_coloring(graph, num_colors)

if colors:
    print("Vertex \tColor")
    for vertex, color in colors.items():
        print(f"{vertex} \t{color}")
else:
    print("No solution exists.")

























































#
#
#
#
#
# def graph_coloring(graph, num_colors):
#     vertices = list(graph.keys())
#     colors = {vertex: -1 for vertex in vertices}
#
#     if graph_coloring_util(graph, num_colors, colors, 0, vertices):
#         return colors
#     else:
#         return None
#
# EXPLAIN THIS IN BRIEF
# ChatGPT
# Certainly! The graph_coloring function is responsible for performing graph coloring. Here's a brief explanation of its functionality:
#
# The function takes two inputs: graph, which represents the graph structure, and num_colors, which specifies the number of colors available for coloring the graph.
# It starts by extracting the vertices from the graph dictionary using the keys() method and storing them in the vertices list.
# It initializes a colors dictionary, where each vertex is initially assigned the color -1. This serves as a placeholder indicating that no color has been assigned yet.
# The function then calls the graph_coloring_util helper function, passing the graph, number of colors, colors dictionary, starting vertex index of 0, and the list of vertices.
# If the graph_coloring_util function returns True, indicating a valid coloring was found, the function returns the colors dictionary.
# Otherwise, if the graph_coloring_util function returns False, indicating no valid coloring exists, the function returns None.
# In summary, the graph_coloring function sets up the initial data structures and invokes the graph_coloring_util




#
#
# def graph_coloring(graph, num_colors):
#     vertices = list(graph.keys())
#     colors = {vertex: -1 for vertex in vertices}
#
#     if graph_coloring_util(graph, num_colors, colors, 0, vertices):
#         return colors
#     else:
#         return None
#
# EXPLAIN THIS IN BRIEF
# ChatGPT
# Certainly! The graph_coloring function is responsible for performing graph coloring. Here's a brief explanation of its functionality:
#
# The function takes two inputs: graph, which represents the graph structure, and num_colors, which specifies the number of colors available for coloring the graph.
# It starts by extracting the vertices from the graph dictionary using the keys() method and storing them in the vertices list.
# It initializes a colors dictionary, where each vertex is initially assigned the color -1. This serves as a placeholder indicating that no color has been assigned yet.
# The function then calls the graph_coloring_util helper function, passing the graph, number of colors, colors dictionary, starting vertex index of 0, and the list of vertices.
# If the graph_coloring_util function returns True, indicating a valid coloring was found, the function returns the colors dictionary.
# Otherwise, if the graph_coloring_util function returns False, indicating no valid coloring exists, the function returns None.
# In summary, the graph_coloring function sets up the initial data structures and invokes the graph_coloring_util



#
# def is_valid_color(graph, colors, vertex, color):
#     for adjacent_vertex in graph[vertex]:
#         if colors[adjacent_vertex] == color:
#             return False
#     return True
#
# # Example usage
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'C', 'D'],
#     'C': ['A', 'B', 'D'],
#     'D': ['B', 'C']
# }
# num_colors = 3
#
# colors = graph_coloring(graph, num_colors)
#
# if colors:
#     print("Vertex \tColor")
#     for vertex, color in colors.items():
#         print(f"{vertex} \t{color}")
# else:
#     print("No solution exists.")
#
#
# eXPLAIN THIS IN BRIEF
#
# ChatGPT
# The is_valid_color function is a utility function used to check whether a given color assignment for a vertex is valid in the graph coloring problem. Here's a brief explanation of its functionality:
#
# The function takes four inputs: graph, which represents the graph structure, colors, a dictionary storing the assigned colors for each vertex, vertex, the vertex for which the color assignment is being checked, and color, the color being considered for the vertex.
# It iterates over each adjacent_vertex of the vertex in the graph.
# For each adjacent_vertex, it checks if the color assigned to it in the colors dictionary is the same as the color being considered for the current vertex.
# If there is any adjacent vertex with the same color, it means that the color assignment is invalid since adjacent vertices should have different colors in a proper graph coloring.
# In that case, the function returns False to indicate that the color assignment is not valid.
# If no adjacent vertices have the same color, the function returns True to indicate that the color assignment is valid for the current vertex.
# The graph coloring algorithm uses this function to check the validity of color assignments during the backtracking process.
# In the example usage, a graph is defined with vertices 'A', 'B', 'C', and 'D', along with their adjacency lists. The graph_coloring function is called with this graph and num_colors set to 3 to find a valid coloring. If a valid coloring is found, it prints the vertex-color assignments; otherwise, it prints a message indicating that no solution exists.
#
# Note: In the given example, the graph is represented using an adjacency list where each vertex is associated with a list of adjacent vertices.
#
#
# Constraint Satisfaction Problem (CSP) is a problem-solving paradigm where the goal is to find a solution that satisfies a set of constraints. CSPs are commonly used in various domains such as artificial intelligence, operations research, and scheduling.
#
# Graph coloring is a classic example of a CSP. The goal is to assign colors to the vertices of a graph such that no adjacent vertices have the same color. The constraints are that adjacent vertices must have different colors.
#
# Branch and Bound and Backtracking are two commonly used techniques to solve CSPs like graph coloring problems. Here's an explanation of each technique:
#
# Backtracking:
#
# Backtracking is a systematic search algorithm that explores the search space by incrementally building a solution and backtracking when constraints are violated.
# The algorithm starts with an empty assignment of colors to vertices and proceeds to assign colors to vertices one by one.
# At each step, it selects a vertex and tries different colors for that vertex.
# If a color assignment violates a constraint (two adjacent vertices have the same color), the algorithm backtracks and tries a different color for the previous vertex.
# The process continues until a valid assignment is found for all vertices or it is determined that no valid assignment is possible.
# Branch and Bound:
#
# Branch and Bound is an optimization technique used to search for the best solution among a large solution space.
# It combines systematic search (like backtracking) with the pruning of branches that are guaranteed to lead to suboptimal solutions.
# In the context of graph coloring, Branch and Bound can be used to find the minimum number of colors required to color the graph optimally.
# The algorithm starts with an initial coloring and uses bounds (lower and upper bounds on the number of colors) to guide the search process.
# It branches into different color assignments and evaluates each branch based on the bounds.
# If a branch's lower bound exceeds the current upper bound, the branch is pruned (i.e., not explored further).
# The algorithm continues branching and backtracking until the optimal solution is found or all branches have been pruned.
# To solve a graph coloring problem using Branch and Bound and Backtracking:
#
# Start with an initial coloring (possibly an empty assignment) and set the upper bound to a large value.
# Use backtracking to incrementally assign colors to vertices, checking the validity of each assignment.
# Update the upper bound whenever a better solution (lower number of colors) is found.
# Apply pruning techniques based on bounds to eliminate unpromising branches during the search.
# Continue the search until an optimal solution (minimum number of colors) is found or it is determined that no valid solution exists.
# Note that the specific implementation details, such as data structures, heuristics, and pruning strategies, may vary depending on the problem and algorithm design.

