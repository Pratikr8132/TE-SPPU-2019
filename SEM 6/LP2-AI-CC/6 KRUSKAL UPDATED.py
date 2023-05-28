def kruskal_mst(graph):
    vertices = list(graph.keys())
    edges = []

    # Create a list of all edges in the graph
    for u in vertices:
        for v, weight in graph[u].items():
            edges.append((u, v, weight))

    # Sort the edges based on their weights
    edges.sort(key=lambda x: x[2])

    parent = {v: v for v in vertices}
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
# graph = {
#     'A': {'B': 5, 'C': 2},
#     'B': {'A': 5, 'C': 4, 'D': 2, 'E': 10},
#     'C': {'A': 2, 'B': 4, 'D': 7, 'E': 11},
#     'D': {'B': 2, 'C': 7, 'E': 5},
#     'E': {'B': 10, 'D': 5, 'C': 4}
# }

graph = {
    'A':{'D':4,'F':5,'B':2},
    'D':{'A':4,'B':1,'E':2},
    'F':{'A':5,'B':8,'G':1},
    'C':{'B':7,'E':10,'G':6},
    'B':{'A':2,'D':1,'E':3,'C':7,'F':8,'G':4},
    'E':{'B':3,'D':2,'C':10},
    'G':{'C':6,'B':4,'F':1}
}


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
#
#
#
#
#
#
#
# Certainly! Let's go through the code line by line:
#
# python
# Copy code
# def kruskal_mst(graph):
#     vertices = list(graph.keys())
#     edges = []
#
#     # Create a list of all edges in the graph
#     for u in vertices:
#         for v, weight in graph[u].items():
#             edges.append((u, v, weight))
# The kruskal_mst function takes a graph represented as a dictionary as input.
# It begins by extracting the list of vertices from the dictionary keys and initializes an empty list edges to store the edges of the graph.
# The nested loop iterates over each vertex u and its adjacent vertices v along with their corresponding edge weights weight.
# Each edge (u, v, weight) is appended to the edges list.
# python
# Copy code
#     # Sort the edges based on their weights
#     edges.sort(key=lambda x: x[2])
#
#     parent = {v: v for v in vertices}
#     mst = []
#     mst_weight = 0
# The edges list is sorted based on the third element of each tuple, which represents the weight of the edge.
# A parent dictionary is created to keep track of the parent of each vertex during the process of finding the minimum spanning tree (MST).
# An empty mst list is initialized to store the edges of the MST, and mst_weight is set to 0 to keep track of the total weight of the MST.
# python
# Copy code
#     # Perform a greedy search on the sorted edges
#     for edge in edges:
#         u, v, weight = edge
#
#         # Find the parent vertices of u and v
#         parent_u = find(parent, u)
#         parent_v = find(parent, v)
#
#         # Add the edge to the MST if it doesn't form a cycle
#         if parent_u != parent_v:
#             mst.append((u, v))
#             mst_weight += weight
#
#             # Merge the two sets by updating the parent
#             parent[parent_u] = parent_v
# The code iterates over each edge (u, v, weight) in the sorted edges list.
# The find function is called to find the parent vertices of u and v using the parent dictionary.
# If the parent vertices are not the same, it means adding the edge (u, v) to the MST will not form a cycle.
# In that case, the edge is added to the mst list, and the mst_weight is updated.
# The two sets are merged by updating the parent of parent_u to parent_v.
# python
# Copy code
#     return mst, mst_weight
#
# def find(parent, vertex):
#     # Find the parent of a vertex
#     if parent[vertex] != vertex:
#         parent[vertex] = find(parent, parent[vertex])
#     return parent[vertex]
# The kruskal_mst function returns the MST represented as a list of edges (mst) and the total weight of the MST (mst_weight).
# The find function is a helper function that implements the path compression technique to find the parent of a vertex.
# It recursively calls itself until it reaches the root parent of a vertex and updates the parent of each visited vertex to the root parent.
# python
# Copy code
# # Example usage
# graph = {
#     'A':{'D':4,'F':5,'B':2},
#     'D':{'A':4,'B':1,'E':2},
#     'F':{'A':5,'B':8,'G':1},
#     'C':{'B':7,'E':10,'G':6},
#     'B':{'A':2,'D':1,'E':3,'C':7,'F':8,'G':4},
#     'E':{'B':3,'D':2,'C':10},
#     'G':{'C':6,'B':4,'F':1}
# }
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
# The code provided at the end demonstrates an example usage of the kruskal_mst function using the graph dictionary.
# The MST edges and their corresponding weights are printed out using a loop over the mst list.
# The total weight of the MST is also printed.
# The Kruskal's algorithm aims to find the minimum spanning tree of a graph by iteratively adding the edges with the smallest weights that do not form a cycle. The algorithm uses a disjoint set data structure (implemented through the parent dictionary) to efficiently detect cycles and merge disjoint sets.






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
