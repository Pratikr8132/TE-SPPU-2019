def kruskal_mst(graph):
    num_vertices = len(graph)
    edges = []

    # Create a list of all edges in the graph
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    # Sort the edges based on their weights
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(num_vertices)]
    mst = []
    mst_weight = 0

    # Perform a greedy search on the sorted edges
    for edge in edges:
        u, v, weight = edge

        # Find the parent vertices of u and v
        parent_u = find(parent, u)
        parent_v = find(parent, v)

        # Add the edge to the MST if it doesn't form a cycle
        if parent_u != parent_v:
            mst.append((u, v))
            mst_weight += weight

            # Merge the two sets by updating the parent
            parent[parent_u] = parent_v

    return mst, mst_weight

def find(parent, vertex):
    # Find the parent of a vertex
    if parent[vertex] != vertex:
        parent[vertex] = find(parent, parent[vertex])
    return parent[vertex]

# Example usage
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst, mst_weight = kruskal_mst(graph)

# Print the MST edges and their weights
print("Edge \tWeight")
for edge in mst:
    u, v = edge
    weight = graph[u][v]
    print(f"{u} - {v}\t{weight}")
print("Total Weight:", mst_weight)



































#
#
# Certainly! Here's a line-by-line explanation of the provided implementation of Kruskal's Minimal Spanning Tree Algorithm:
#
# python
# Copy code
# def kruskal_mst(graph):
#     num_vertices = len(graph)
#     edges = []
#
#     # Create a list of all edges in the graph
#     for i in range(num_vertices):
#         for j in range(i + 1, num_vertices):
#             if graph[i][j] != 0:
#                 edges.append((i, j, graph[i][j]))
# The kruskal_mst function takes a graph represented as an adjacency matrix.
# It initializes the number of vertices in the graph and an empty list called edges.
# The nested loops iterate through the upper triangle of the adjacency matrix to create a list of all edges in the graph. If the weight of the edge between vertices i and j is non-zero, it is added to the edges list as a tuple (i, j, weight).
# python
# Copy code
#     # Sort the edges based on their weights
#     edges.sort(key=lambda x: x[2])
# The edges list is sorted based on the third element of each tuple, which represents the weight of the edge. This sorting step ensures that the edges are considered in non-decreasing order of weight during the greedy search.
# python
# Copy code
#     parent = [i for i in range(num_vertices)]
#     mst = []
#     mst_weight = 0
# The parent list is initialized, where each vertex initially points to itself as its parent. This list will be used to track the parent vertex of each vertex in the MST.
# The mst list is initialized as an empty list, which will store the edges in the MST.
# The mst_weight variable is initialized to 0, representing the total weight of the MST.
# python
# Copy code
#     for edge in edges:
#         u, v, weight = edge
#
#         # Find the parent vertices of u and v
#         parent_u = find(parent, u)
#         parent_v = find(parent, v)
# The algorithm iterates through each edge in the sorted edges list.
# The vertices and weight of the current edge are unpacked into variables u, v, and weight.
# The find function is called to find the parent vertices of u and v. This function utilizes path compression to efficiently find the ultimate parent of a vertex.
# python
# Copy code
#         if parent_u != parent_v:
#             mst.append((u, v))
#             mst_weight += weight
#
#             # Merge the two sets by updating the parent
#             parent[parent_u] = parent_v
# If the parent vertices of u and v are not the same, it means that adding the current edge to the MST will not form a cycle.
# In this case, the current edge is added to the mst list, and its weight is added to mst_weight.
# The parent vertex of parent_u is updated to parent_v, effectively merging the two sets (or trees) in the MST.
# python
# Copy code
#     return mst, mst_weight
# Once the iteration through all edges is complete, the function returns the mst list, representing the edges in the MST, and mst_weight, representing the total weight of the MST.
# python
# Copy code
# def find(parent, vertex):
#     # Find the parent of a vertex
#     if parent[vertex] != vertex:
#         parent[vertex] = find(parent, parent[vertex])
#     return parent[vertex]
# The find function is a helper function used to find the ultimate parent of a vertex in the MST.
# It uses path compression to optimize future lookups by directly updating the parent of a vertex to its ultimate parent during the recursive call.
# The function returns the ultimate parent of the vertex.
# The remaining part of the code demonstrates example usage. It creates a sample graph, calls the kruskal_mst function, and prints the edges in the MST along with their weights.
#
# I hope this# detailed explanation helps you understand the implementation. Let me know if you have any further questions!


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

#
# graph = [
#     [0, 4, 0, 0, 0, 0, 0, 8, 0],
#     [4, 0, 8, 0, 0, 0, 0, 11, 0],
#     [0, 8, 0, 7, 0, 4, 0, 0, 2],
#     [0, 0, 7, 0, 9, 14, 0, 0, 0],
#     [0, 0, 0, 9, 0, 10, 0, 0, 0],
#     [0, 0, 4, 14, 10, 0, 2, 0, 0],
#     [0, 0, 0, 0, 0, 2, 0, 1, 6],
#     [8, 11, 0, 0, 0, 0, 1, 0, 7],
#     [0, 0, 2, 0, 0, 0, 6, 7, 0]
# ]
#
# mst, mst_weight = kruskal_mst(graph)
#
# # Print the MST edges and their weights
# print("Edge \tWeight")
# for edge in mst:
#     u, v = edge
#     weight = graph[u][v]
#     print(f"{u} - {v}\t{weight}")
# print("Total Weight:", mst_weight)
# Output:
#
# mathematica
# Copy code
# Edge    Weight
# 0 - 1    4
# 2 - 8    2
# 3 - 4    9
# 2 - 3    7
# 5 - 6    2
# 0 - 7    8
# 2 - 5    4
# Total Weight: 37