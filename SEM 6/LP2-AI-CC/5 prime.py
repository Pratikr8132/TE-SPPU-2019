
import sys

def prim_mst(graph):
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices
    parent = [None] * num_vertices
    mst_set = [False] * num_vertices

    key[0] = 0  # Start with the first vertex

    for _ in range(num_vertices - 1):
        u = min_key(key, mst_set)
        mst_set[u] = True

        for v in range(num_vertices):
            if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent

def min_key(key, mst_set):
    min_value = sys.maxsize
    min_index = None

    for v in range(len(key)):
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_index = v

    return min_index
# Example usage
graph = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]


mst_parent = prim_mst(graph)

# Print the MST edges and their weights
print("Edge \tWeight")
for i in range(1, len(graph)):
    print(f"{mst_parent[i]} - {i}\t{graph[i][mst_parent[i]]}")





#
# graph = [
#     [0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0]
# # ]
# graph = [
#     [0, 1, 0, 2, 0],
#     [1, 0, 3, 4, 0],
#     [0, 3, 0, 5, 6],
#     [2, 4, 5, 0, 7],
#     [0, 0, 6, 7, 0]
# ]
































#
#
#
###########algorithmmmmmmmmmmmmmm--------->
#
# User
# Prim's Minimal Spanning Tree Algorithm definition and tell me how it works
#
# ChatGPT
# Prim's algorithm is a greedy algorithm used to find the minimum spanning tree (MST) in a connected, weighted graph. The minimum spanning tree is a subset of the graph's edges that connects all vertices together with the minimum total weight.
#
# Here's a step-by-step description of how Prim's Minimal Spanning Tree Algorithm works:
#
# Start with an empty set of edges, which represents the MST.
# Choose an arbitrary vertex as the starting vertex and add it to the MST.
# Repeat the following steps until all vertices are included in the MST:
# Among the edges that connect the vertices in the MST to the vertices not yet in the MST, find the edge with the minimum weight. This edge will be added to the MST.
# Add the selected edge to the MST and mark the corresponding vertex as visited.
# The algorithm terminates when all vertices are included in the MST.
# In more detail, here's the step-by-step process:
#
# Initialize an empty MST and a data structure to track the visited vertices.
# Choose an arbitrary vertex as the starting vertex and add it to the MST.
# While there are still unvisited vertices:
# Look at the edges that connect the visited vertices (in the MST) to the unvisited vertices.
# Choose the edge with the minimum weight.
# Add this edge to the MST.
# Mark the corresponding unvisited vertex as visited.
# The algorithm continues until all vertices are included in the MST.
# The final result is the MST, which consists of the selected edges.
# The main idea behind Prim's algorithm is to grow the MST incrementally by always selecting the edge with the minimum weight. At each step, the algorithm considers the set of visited vertices and looks for the minimum-weight edge that connects them to the unvisited vertices. This ensures that the selected edges form a tree with the minimum total weight.
#
# Prim's algorithm is a good choice for finding the MST when the graph is dense or when there are fewer edges than vertices. It has a time complexity of O(V^2) using an adjacency matrix representation, and it can be optimized to O(E log V) using a priority queue.
#
# I hope this explanation clarifies the concept and working of Prim's Minimal Spanning Tree Algorithm. Let me know if you have any further questions!


#
#
#
#
# Certainly! Here's an explanation of the code line by line:
#
# python
# Copy code
# import sys
# This line imports the sys module, which provides access to system-specific parameters and functions.
#
# python
# Copy code
# def prim_mst(graph):
#     num_vertices = len(graph)
#     key = [sys.maxsize] * num_vertices
#     parent = [None] * num_vertices
#     mst_set = [False] * num_vertices
#
#     key[0] = 0  # Start with the first vertex
# The prim_mst function takes a graph represented as an adjacency matrix. It initializes some variables: num_vertices stores the number of vertices in the graph, key represents the minimum key values to reach each vertex, parent stores the parent vertex of each vertex in the MST, and mst_set keeps track of vertices included in the MST. The key value of the starting vertex is set to 0.
#
# python
# Copy code
#     for _ in range(num_vertices - 1):
#         u = min_key(key, mst_set)
#         mst_set[u] = True
# This loop runs num_vertices - 1 times, as the MST will have num_vertices - 1 edges. It finds the vertex u with the minimum key value among the vertices not yet included in the MST, using the min_key helper function. The variable u is marked as part of the MST by setting mst_set[u] to True.
#
# python
# Copy code
#         for v in range(num_vertices):
#             if graph[u][v] != 0 and not mst_set[v] and graph[u][v] < key[v]:
#                 key[v] = graph[u][v]
#                 parent[v] = u
# This nested loop iterates over all the vertices v. It checks if there is an edge between u and v (graph[u][v] != 0), if v is not already in the MST (not mst_set[v]), and if the weight of the edge u-v is smaller than the current key value of v. If these conditions are satisfied, the key value of v is updated with the weight of the u-v edge, and the parent of v is set to u.
#
# python
# Copy code
#     return parent
# After the loops complete, the function returns the parent array, which represents the MST.
#
# python
# Copy code
# def min_key(key, mst_set):
#     min_value = sys.maxsize
#     min_index = None
#
#     for v in range(len(key)):
#         if key[v] < min_value and not mst_set[v]:
#             min_value = key[v]
#             min_index = v
#
#     return min_index
# The min_key function takes the key array and the mst_set array as input. It finds the vertex with the minimum key value among the vertices not yet included in the MST. It initializes min_value with the maximum integer value, and min_index with None. It then iterates over the indices of key and checks if the key value at index v is smaller than min_value and if v is not yet included in the MST. If these conditions are met, min_value and min_index are updated accordingly. Finally, the function returns min_index, which represents the vertex with the minimum key value.
#
# The remaining lines of code provide an example usage of the prim_mst function with a sample graph, and then print the edges and their weights in the MST.
#
# I hope this expla


#
#
#
# tell me the difference between the three kruskals dijkstra prime and uses in real life time complexity and what data types they use and many more like this
#
# ChatGPT
# Certainly! Here's a detailed comparison between Kruskal's algorithm, Dijkstra's algorithm, and Prim's algorithm:
#
# Kruskal's Algorithm:
#
# Purpose: Find a minimum spanning tree (MST) in a connected, weighted, undirected graph.
# Data Structures Used: Disjoint Set Union (DSU) data structure, Graph (Adjacency List or Matrix).
# Time Complexity: O(E log E) or O(E log V) using a Union-Find data structure.
# Applications: Network design, circuit wiring, transportation networks, clustering, approximation algorithms.
# Dijkstra's Algorithm:
#
# Purpose: Find the shortest path between a source vertex and all other vertices in a weighted graph.
# Data Structures Used: Priority Queue, Graph (Adjacency List or Matrix).
# Time Complexity: O((V + E) log V) using a binary heap.
# Applications: Routing protocols, network analysis, GPS navigation, resource allocation.
# Prim's Algorithm:
#
# Purpose: Find a minimum spanning tree (MST) in a connected, weighted, undirected graph.
# Data Structures Used: Priority Queue, Graph (Adjacency List or Matrix).
# Time Complexity: O((V + E) log V) using a binary heap.
# Applications: Network design, clustering, image segmentation, approximate algorithms for optimization problems.
# Key Differences:
#
# Kruskal's algorithm finds an MST by considering edges in ascending order of weights, while Prim's algorithm grows the MST by adding vertices in a greedy manner.
# Kruskal's algorithm uses the Disjoint Set Union (DSU) data structure to efficiently check for cycles and merge components.
# Dijkstra's algorithm is used for finding the shortest path, while Kruskal's and Prim's algorithms are used for finding the MST.
# Dijkstra's algorithm considers the weights of edges, while Kruskal's and Prim's algorithms consider the weights of edges or the connectivity of vertices.
# Kruskal's and Prim's algorithms work on undirected graphs, while Dijkstra's algorithm can handle directed graphs as well.
# Real-life Examples:
#
# Kruskal's algorithm: Constructing power grids, designing transportation networks, circuit board wiring, finding clusters in data analysis.
# Dijkstra's algorithm: GPS navigation systems, routing in computer networks, finding the shortest path in transportation networks, optimizing resource allocation.
# Prim's algorithm: Designing communication networks, cluster analysis, identifying areas of high connectivity in social networks, image segmentation.
# Note: The time complexity mentioned above assumes using a binary heap as the priority queue in Dijkstra's and Prim's algorithms. Other data structures, such as Fibonacci heap, can achieve better time complexity for certain cases.
#


# I hope this comparison provides you with a comprehensive understanding of the differences, real-life applications, time complexities, and data structures used in these algorithms. Let me know if you have any further questions!
