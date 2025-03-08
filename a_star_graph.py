import heapq

def a_star_graph_search(graph, heuristic, start, goal):
    priority_queue = [(0 + heuristic[start], 0, [start])]  # (f = g + h, g, path)
    visited = set()  # Menyimpan simpul yang telah dieksplorasi

    while priority_queue:
        f, g, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node in visited:
            continue  # Lewati simpul yang sudah dikunjungi
        visited.add(node)

        if node == goal:
            return path, g  # Mengembalikan jalur dan biaya total

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + cost  # Biaya langkah (g)
                new_f = new_g + heuristic[neighbor]  # f = g + h
                heapq.heappush(priority_queue, (new_f, new_g, path + [neighbor]))

    return None, float('inf')  # Jika tidak ditemukan jalur

# Definisi graf dengan bobot sebagai adjacency list
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

# Nilai heuristik untuk setiap simpul
heuristic = {
    'A': 6, 'B': 4, 'C': 4,
    'D': 2, 'E': 2, 'F': 3,
    'G': 0  # Heuristik tujuan harus 0
}

# Jalankan A* Graph Search
start_node = 'A'
goal_node = 'G'
path, cost = a_star_graph_search(graph, heuristic, start_node, goal_node)

print("A* Graph Search Path:", path)
print("Total Cost:", cost)
