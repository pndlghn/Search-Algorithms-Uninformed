# Uniform Cost Search (UCS) Implementation
import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, [start])]
    visited = set()
    
    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]
        print("Visiting:", node, "with cost:", cost)
        
        if node == goal:
            return path, cost
        
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(priority_queue, (cost + weight, new_path))
    
    return None, float('inf')

if __name__ == "__main__":
    example_graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 3)],
        'D': [('G', 1)],
        'E': [('G', 2)],
        'F': [('G', 2)],
        'G': []
    }
    path, cost = ucs(example_graph, 'A', 'G')
    print("UCS Path:", path, "with minimum cost:", cost)
