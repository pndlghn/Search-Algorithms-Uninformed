# Breadth-First Search (BFS) Implementation
from collections import deque

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        print("Visiting:", node)
        
        if node == goal:
            return path
        
        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return None

if __name__ == "__main__":
    example_graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': ['G'],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    print("BFS Path:", bfs(example_graph, 'A', 'G'))
