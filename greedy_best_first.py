import heapq

def greedy_best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start)]  # (heuristik, simpul)
    visited = set()
    path = []

    while priority_queue:
        _, node = heapq.heappop(priority_queue)  # Ambil simpul dengan heuristik terkecil

        if node in visited:
            continue
        visited.add(node)
        path.append(node)
        
        print("Visiting:", node)  # Cetak urutan kunjungan
        
        if node == goal:
            return path  # Jika mencapai tujuan, kembalikan jalur

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))

    return None  # Jika tidak ditemukan jalur

# Definisi graf sebagai adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

# Nilai heuristik untuk setiap simpul
heuristic = {
    'A': 6, 'B': 4, 'C': 4,
    'D': 2, 'E': 2, 'F': 3,
    'G': 0  # Heuristik tujuan harus 0
}

# Jalankan Greedy Best-First Search
start_node = 'A'
goal_node = 'G'
path = greedy_best_first_search(graph, heuristic, start_node, goal_node)

print("GBFS Path:", path)
