import heapq


def greedy_mst(graph):
    start_node = list(graph.keys())[0]
    visited = set()
    mst = []

    # Create a priority queue to store nodes with their costs
    pq = [(0, start_node)]

    while pq:
        cost, current_node = heapq.heappop(pq)

        if current_node not in visited:
            visited.add(current_node)
            mst.append((cost, current_node))

            # Visit neighbors and update their costs in the priority queue
            for neighbor, edge_cost in graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_cost, neighbor))

    return mst


# Driver code

# Define the graph
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 4, 'D': 2,'E' : 10},
    'C': {'A': 2, 'B': 4, 'D': 7,'E':11},
    'D': {'B': 2, 'C': 7,'E':5},
    'E': {'B':10,'D':5,'C':4}
}

# Run the Greedy MST algorithm
mst = greedy_mst(graph)

# Print the Minimum Spanning Tree
print("Minimum Spanning Tree:")
for cost, node in mst:
    print(f"{node} - {cost}")
print("total cost:")

























#
#
#
#
#
#
#
#
# Sure! Here's an explanation of each line of the code and some questions related to it:
#
# python
# Copy code
# import heapq
# This line imports the heapq module, which provides functions for working with a priority queue.
#
# python
# Copy code
# def greedy_mst(graph):
# This line defines the greedy_mst function that takes a graph as input and computes the Minimum Spanning Tree (MST) using a greedy algorithm.
#
# python
# Copy code
#     start_node = list(graph.keys())[0]
# This line selects the first node in the graph as the starting node for the MST construction.
#
# python
# Copy code
#     visited = set()
#     mst = []
# These lines initialize an empty set visited to keep track of visited nodes and an empty list mst to store the MST.
#
# python
# Copy code
#     pq = [(0, start_node)]
# This line initializes a priority queue pq with a single element, which is a tuple (0, start_node). The tuple represents the cost (initialized as 0) and the current node.
#
# python
# Copy code
#     while pq:
# This line starts a loop that continues until the priority queue pq is empty.
#
# python
# Copy code
#         cost, current_node = heapq.heappop(pq)
# This line pops the element with the smallest cost from the priority queue pq and assigns its cost and current node to the variables cost and current_node.
#
# python
# Copy code
#         if current_node not in visited:
# This line checks if the current node has not been visited before.
#
# python
# Copy code
#             visited.add(current_node)
#             mst.append((cost, current_node))
# These lines add the current node to the visited set and append the tuple (cost, current_node) to the MST list.
#
# python
# Copy code
#             for neighbor, edge_cost in graph[current_node].items():
# This line iterates over the neighbors of the current node along with their edge costs.
#
# python
# Copy code
#                 if neighbor not in visited:
#                     heapq.heappush(pq, (edge_cost, neighbor))
# These lines check if the neighbor has not been visited and push it into the priority queue pq with its edge cost.
#
# python
# Copy code
#     return mst
# This line returns the Minimum Spanning Tree (mst) once the algorithm has finished.
#
# python
# Copy code
# graph = {
#     'A': {'B': 5, 'C': 2},
#     'B': {'A': 5, 'C': 4, 'D': 2},
#     'C': {'A': 2, 'B': 4, 'D': 7},
#     'D': {'B': 2, 'C': 7}
# }
# This block of code defines the input graph as a dictionary, where each key represents a node, and the corresponding value is another dictionary containing neighbors and their edge costs.
#
# python
# Copy code
# mst = greedy_mst(graph)
# This line invokes the greedy_mst function with the input graph and assigns the result (MST) to the variable mst.
#
# python
# Copy code
# print("Minimum Spanning Tree:")
# for cost, node in mst:
#     print(f"{node} - {cost}")
# These lines print the Minimum Spanning Tree by iterating over the elements in mst and printing the node and its associated cost.
#
# Potential questions:
#
#
# tell me the difference between the three kruskals dijkstra prime and uses in real life time complexity and what data types they use and many more like this
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