import heapq


def dijkstra(graph, start_node, goal_node):
    distances = {node: float('inf') for node in graph}
    distances[start_node] = 0
    previous_nodes = {node: None for node in graph}

    # Create a priority queue to store nodes with their distances
    pq = [(0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == goal_node:
            break  # Stop the algorithm if the goal node is reached

        if current_distance > distances[current_node]:
            continue

        for neighbor, edge_weight in graph[current_node].items():
            distance = current_distance + edge_weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    # Build the shortest path from start to goal
    path = []
    current = goal_node
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()

    return distances[goal_node], path


# Driver code

# Define the graph
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 4, 'D': 2,'E' : 10},
    'C': {'A': 2, 'B': 4, 'D': 7,'E':11},
    'D': {'B': 2, 'C': 7,'E':5},
    'E': {'B':10,'D':5,'C':4}
}

start_node = 'A'
goal_node = 'E'

# Run Dijkstra's algorithm from start to goal
distance, path = dijkstra(graph, start_node, goal_node)

# Print the shortest path and distance
print(f"Shortest path from {start_node} to {goal_node}:")
print(" -> ".join(path))
print("Distance:", distance)































#
#
# #
# Certainly! Here's an explanation of the code line by line:
#
# Import the heapq module, which provides an implementation of the heap queue algorithm.
#
# Define the dijkstra function that takes in the graph, start_node, and goal_node as parameters. This function will implement Dijkstra's algorithm to find the shortest path from the start node to the goal node.
#
# Create a dictionary called distances to store the shortest distances from the start node to each node in the graph. Initialize all distances with float('inf') except for the start node, which is set to 0.
#
# Create a dictionary called previous_nodes to store the previous node in the shortest path for each node in the graph. Initialize all nodes with None.
#
# Create a priority queue pq using a list to store nodes with their distances. The priority queue will be used to select the node with the smallest distance during each iteration of the algorithm. Initialize it with a tuple (0, start_node), indicating the distance from the start node to itself is 0.
#
# Start a while loop that continues until the priority queue pq is empty.
#
# Extract the node with the smallest distance from the priority queue. This is done using the heapq.heappop() function, which extracts the smallest item based on the first element of each tuple (the distance).
#
# Check if the current node is the goal node. If it is, break the loop as we have found the shortest path from the start node to the goal node.
#
# Check if the current distance is greater than the stored distance for the current node in the distances dictionary. If it is, continue to the next iteration of the loop. This is to avoid processing nodes multiple times if a shorter path to them has already been found.
#
# Iterate through the neighbors of the current node and their corresponding edge weights.
#
# Calculate the new distance to the neighbor by adding the current distance and the edge weight.
#
# If the new distance is smaller than the stored distance for the neighbor in the distances dictionary, update the distance, set the current node as the previous node for the neighbor, and push a tuple (distance, neighbor) to the priority queue pq. This ensures that the neighbor will be processed in the future with the updated distance.
#
# Build the shortest path from the start node to the goal node by iterating from the goal node to the start node using the previous_nodes dictionary. Append each node to the path list.
#
# Reverse the order of the path list to obtain the correct order from the start node to the goal node.
#
# Return the shortest distance and the path as the output of the dijkstra function.
#
# Define the graph as a dictionary where the keys represent nodes, and the values represent dictionaries containing the neighbors of each node along with their corresponding edge weights.
#
# Set the start_node and goal_node for which we want to find the shortest path.
#
# Call the dijkstra function with the provided graph, start_node, and goal_node. Store the returned distance and path.
#
# Print the shortest path from the start node to the goal node by joining the nodes in the path list using the ' -> ' separator.
#
# Print the total distance of the shortest path.
#
# Print the path followed by iterating through the path list and printing each edge in the format "current_node -> next_node: edge_weight".
#
# I hope this explanation helps you understand the code. Let me know if you have any further questions!

# #Dijkstra's algorithm is a graph traversal algorithm used to find the shortest path between a starting node and all other nodes in a weighted graph. It works by iteratively selecting the node with the smallest distance from the starting node and updating the distances to its neighboring nodes.
#
# Here's a step-by-step explanation of how Dijkstra's algorithm works:
#
# Start by assigning a tentative distance value of zero to the starting node and infinity to all other nodes. Set the starting node as the current node.
#
# For the current node, consider all of its neighboring nodes and calculate their tentative distances from the starting node through the current node. Compare these calculated distances with the current assigned values, and if the calculated distance is smaller, update the assigned distance.
#
# Once all the neighbors of the current node have been considered, mark the current node as "visited" to indicate that its distance has been finalized.
#
# Select the unvisited node with the smallest tentative distance as the new current node and repeat steps 2 and 3.
#
# Repeat steps 2 to 4 until all nodes have been visited. The algorithm is complete when the goal node (if specified) is visited, or when all nodes have been visited.
#
# After the algorithm finishes, the shortest distance to each node from the starting node is determined, and the shortest path can be reconstructed by following the previous nodes from the goal node back to the starting node.
#
# Now, let's go through some questions related to the given code along with their answers:
#
# Q1: What does the pq variable represent in the code?
# A1: The pq variable represents the priority queue used to store nodes with their distances during the execution of Dijkstra's algorithm. It is implemented as a list where each element is a tuple containing the distance and the node.
#
# Q2: How does the algorithm ensure that the smallest distance nodes are selected from the priority queue?
# A2: The priority queue pq is implemented using the heapq module, which maintains the heap property. The heapq.heappop() function extracts the smallest element based on the first element of each tuple (the distance). This ensures that the nodes with the smallest distances are always selected first.
#
# Q3: What is the purpose of the previous_nodes dictionary?
# A3: The previous_nodes dictionary is used to keep track of the previous node in the shortest path for each node. It is updated during the execution of the algorithm and allows the reconstruction of the shortest path from the goal node back to the starting node.
#
# Q4: How is the shortest path reconstructed using the previous_nodes dictionary?
# A4: The shortest path is reconstructed by starting from the goal node and following the previous nodes in reverse order until reaching the starting node. Each node is appended to the path list, and then the order is reversed to obtain the correct path from the starting node to the goal node.
#
# Q5: What is the time complexity of Dijkstra's algorithm?
# A5: The time complexity of Dijkstra's algorithm is typically O((V + E) log V), where V is the number of nodes and E is the number of edges in the graph. The use of the priority queue helps optimize the algorithm by selecting the nodes with the smallest distances efficiently.