import sys

def prim_mst(graph):
    vertices = list(graph.keys())
    num_vertices = len(vertices)
    key = {v: sys.maxsize for v in vertices}
    parent = {v: None for v in vertices}
    mst_set = {v: False for v in vertices}

    key[vertices[0]] = 0  # Start with the first vertex

    for _ in range(num_vertices - 1):
        u = min_key(key, mst_set)
        mst_set[u] = True

        for v in graph[u]:
            if not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent

def min_key(key, mst_set):
    min_value = sys.maxsize
    min_vertex = None

    for v in key:
        if key[v] < min_value and not mst_set[v]:
            min_value = key[v]
            min_vertex = v

    return min_vertex

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

mst_parent = prim_mst(graph)

# Print the MST edges and their weights
print("Edge \tWeight")
for v in mst_parent:
    if mst_parent[v] is not None:
        weight = graph[v][mst_parent[v]]
        print(f"{mst_parent[v]} - {v}\t{weight}")
















































# Certainly! Here's a detailed explanation of the code:
#
# The code begins by importing the sys module, which is used for getting the maximum integer value.
#
# The prim_mst function takes the graph as input and returns the parent dictionary representing the minimum spanning tree. It uses the Prim's algorithm to find the minimum spanning tree of the graph.
#
# The vertices variable is assigned a list of all the vertices in the graph. num_vertices stores the number of vertices in the graph.
#
# Three dictionaries, key, parent, and mst_set, are initialized to store the key values, parent vertices, and the status of inclusion in the minimum spanning tree (MST) for each vertex, respectively. Initially, all vertices have a key value of sys.maxsize, parent value of None, and MST inclusion status as False.
#
# The key value of the first vertex (the vertex at index 0 in the vertices list) is set to 0, indicating that it will be selected first in the MST.
#
# The prim_mst function then enters a loop that runs for num_vertices - 1 iterations. This is because the MST will have num_vertices - 1 edges.
#
# Inside the loop, min_key function is called to find the vertex u with the minimum key value among the vertices not yet included in the MST. The mst_set status of u is updated to True, indicating its inclusion in the MST.
#
# The code then iterates over the adjacent vertices v of u in the graph. For each adjacent vertex v, it checks if v is not yet included in the MST, and the weight of the edge between u and v is less than the current key value of v. If both conditions are satisfied, the key value of v is updated to the weight of the edge, and the parent of v is set to u.
#
# After the loop completes, the parent dictionary representing the minimum spanning tree is returned.
#
# The example usage section defines the graph using the dictionary-based representation you provided.
#
# The mst_parent variable stores the minimum spanning tree obtained by calling the prim_mst function with the graph as input.
#
# Finally, the code prints the edges and their weights in the minimum spanning tree. It iterates over each vertex v in the mst_parent dictionary, excluding the first vertex. For each vertex v, if its parent is not None, it retrieves the weight of the edge between v and its parent and prints the edge and weight.
#
# That's the detailed explanation of the code. It applies Prim's algorithm to find the minimum spanning tree of the given graph and prints the edges and their weights in the MST.


#he Prim's algorithm is used to find the minimum spanning tree (MST) of a connected weighted graph. The algorithm starts with an arbitrary vertex and gradually expands the MST by adding the minimum-weight edge that connects a vertex in the MST to a vertex outside the MST. This process continues until all vertices are included in the MST.
#
# Here is a step-by-step algorithm for Prim's minimum spanning tree algorithm:
#
# Create an empty MST set to store the edges of the minimum spanning tree.
# Initialize a key value for each vertex in the graph, representing the minimum weight of an edge connecting that vertex to the MST. Set the key value of the starting vertex to 0 and the key value of all other vertices to infinity.
# Initialize a parent array to store the parent vertex for each vertex in the MST. Set the parent of the starting vertex to None.
# While there are vertices not yet included in the MST, do the following:
# Select a vertex u which has the minimum key value and is not yet included in the MST.
# Add the edge (u, parent[u]) to the MST set.
# Update the key values and parent values of the adjacent vertices of u:
# For each adjacent vertex v of u:
# If v is not yet included in the MST and the weight of the edge (u, v) is less than the current key value of v, update the key value of v to the weight of (u, v) and set the parent of v to u.
# The MST set contains all the edges of the minimum spanning tree.
# The key idea of the Prim's algorithm is to always select the vertex with the minimum key value, ensuring that the edges added to the MST form a tree with minimum weight. By iteratively adding the minimum-weight edges, the algorithm constructs the minimum spanning tree of the graph.
#
# It's important to note that the algorithm assumes the graph is connected, meaning there is a path between any pair of vertices. If the graph is not connected, the algorithm can be applied to each connected component separately to find the minimum spanning forest.
#
#
#
#


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

