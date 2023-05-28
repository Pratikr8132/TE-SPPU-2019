

from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited


# Example usage:
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': ['11', '12'],
    '4': ['55'],
    '8': [],
    '11': [],
    '12': [],
    '55': [],
}

print("Following is the Breadth-First Search")
bfs_result = bfs(graph, '5')
print(bfs_result)

print("Following is the Depth-First Search")
dfs_result = dfs(graph, '5')
print(dfs_result)




























# The code begins with importing the deque class from the collections module. The deque class is a double-ended queue that supports efficient append and pop operations from both ends.
#
# The bfs function implements the breadth-first search algorithm. It takes two parameters: graph, which represents the graph structure as a dictionary, and start_node, which is the node from which the search starts. The function returns the list of visited nodes in the order they were visited.
#
# The visited list is initialized to store the visited nodes, and the queue is initialized as a deque containing the start_node.
#
# The BFS algorithm starts with a while loop that continues until the queue becomes empty. Inside the loop, the leftmost node from the queue is removed using the popleft method of the deque and assigned to the variable node.
#
# If the node is not in the visited list, it means it hasn't been visited before. In that case, the node is appended to the visited list, and its adjacent nodes (obtained from graph[node]) are added to the queue using the extend method.
#
# Finally, when the while loop ends, the function returns the visited list, which contains all the nodes visited during the BFS traversal.
#
# The dfs function implements the depth-first search algorithm. It takes the same parameters as the bfs function and returns the list of visited nodes in the order they were visited.
#
# The visited list is initialized, and the stack is initialized with the start_node.
#
# The DFS algorithm also uses a while loop that continues until the stack becomes empty. Inside the loop, the topmost node from the stack is removed using the pop method and assigned to the variable node.
#
# If the node is not in the visited list, it means it hasn't been visited before. In that case, the node is appended to the visited list, and its adjacent nodes are added to the stack using the extend method.
#
# Finally, when the while loop ends, the function returns the visited list, which contains all the nodes visited during the DFS traversal.
#
# Comparing BFS and DFS:
#
# BFS visits nodes at the same level before moving to the next level, while DFS explores as far as possible along each branch before backtracking.
# BFS uses a queue to store the nodes, ensuring that nodes are visited in the order they were discovered. DFS uses a stack to store nodes, resulting in a last-in-first-out order of traversal.
# BFS guarantees finding the shortest path between two nodes in an unweighted graph, whereas DFS does not guarantee the shortest path.
# Additional Search Algorithms:
#
# There are other search algorithms such as Dijkstra's algorithm, A* search, and depth-limited search, which have different characteristics and use cases.
# Dijkstra's algorithm is a weighted graph search algorithm that finds the shortest path between nodes by considering the edge weights.
# A* search is an informed search algorithm that uses heuristics to guide the search towards the goal node efficiently.
# Depth-limited search is similar to DFS but limits the depth of exploration, preventing it from going too deep into the graph