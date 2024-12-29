# DFS Graph Traversal

def graph_dfs(graph, start, visited=None):
    if visited is None:
        visited = set() # Create a new set to store visited nodes
    visited.add(start) # Add the current node to the visited set
    print("Start Node is: ")
    print(start) # Print the current node
    for neighbor in graph[start]: # Visit all neighbors of the current node
        if neighbor not in visited: # If the neighbor has not been visited
            graph_dfs(graph, neighbor, visited) # Recursively
    return visited # Return the set of visited nodes

def graph_details():
    print("Hello World!")
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'C'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("Full Graph Here:")
    print(graph)
    visited_nodes = graph_dfs(graph, 'A')
    print("Visited Nodes:")
    print(visited_nodes)

def main():
    graph_details()

if __name__ == "__main__":
    main()