# Search-Algorithms-Uninformed

# DFS
Kode di atas mengimplementasikan algoritma Depth-First Search (DFS) untuk mencari jalur dari node awal (start) ke node tujuan (goal) dalam sebuah graph yang direpresentasikan sebagai dictionary. Berikut adalah penjelasan fungsional dari setiap bagian kode:

1. Import dan Definisi Fungsi DFS
```python
def dfs(graph, start, goal, visited=None, path=None):
```
- ``` graph ```: Representasi graph dalam bentuk dictionary.
- ``` start ```: Node awal pencarian.
- ``` goal ```: Node tujuan yang dicari.
- ``` visited ```: Set yang menyimpan node yang telah dikunjungi (default ``` None ```, nanti akan diubah menjadi ``` set() ```).
- ``` path ```: List yang menyimpan jalur yang sedang dieksplorasi (default None, nanti akan diubah menjadi ``` [] ```).
  
2. Inisialisasi visited dan path
```python
if visited is None:
    visited = set()
if path is None:
    path = []
```
- Jika ``` visited ``` belum ada, maka dibuat set kosong.
- Jika ``` path ``` belum ada, maka dibuat list kosong.
  
3. Menandai Node Sebagai Dikunjungi
```python
visited.add(start)
path.append(start)
print("Visiting:", start)
```
- Node ``` start ``` ditandai sebagai telah dikunjungi dengan menambahkannya ke ``` visited ```.
- Node ``` start ``` dimasukkan ke ``` path ``` untuk menyimpan jalur yang sedang dieksplorasi.
- Menampilkan node yang sedang dikunjungi.
  
4. Pengecekan Apakah start Adalah goal
```python
if start == goal:
    return path
```
- Jika node start adalah node tujuan (``` goal ```), maka mengembalikan path sebagai jalur yang ditemukan.
  
5. Melakukan Rekursi DFS ke Tetangga
```python
for neighbor in graph.get(start, []):
    if neighbor not in visited:
        result = dfs(graph, neighbor, goal, visited, path)
        if result:
            return result
```
- Mengiterasi semua tetangga (``` neighbor ```) dari ``` start ```.
- Jika tetangga belum dikunjungi, maka rekursi DFS dipanggil pada tetangga tersebut.
- Jika rekursi menemukan jalur ke ``` goal ```, maka jalur tersebut dikembalikan (``` return result ```).
  
6. Backtracking Jika Tidak Ada Jalur
```python
path.pop()
return None
```
- Jika tidak menemukan jalur ke ``` goal ```, maka node terakhir dihapus dari ``` path ``` (backtracking).
- Mengembalikan ``` None ```, menandakan bahwa jalur ini buntu (dead-end).
  
7. Bagian Main Program
```python
if __name__ == "__main__":
```
- Kode di bawah ini hanya dijalankan jika script dieksekusi secara langsung.

Membuat Graph
```python
example_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
```
- Graph direpresentasikan sebagai dictionary, di mana key adalah node dan value adalah daftar tetangganya.

Menjalankan DFS
```python
print("DFS Path:", dfs(example_graph, 'A', 'G'))
```
- Mencari jalur dari ``` 'A' ``` ke ``` 'G' ``` menggunakan DFS dan menampilkan hasilnya.

Contoh Eksekusi
Jika dijalankan, program akan mencetak urutan node yang dikunjungi dan jalur hasil DFS:

Output:

```pgsql
Visiting: A
Visiting: B
Visiting: D
Visiting: G
DFS Path: ['A', 'B', 'D', 'G']
```
Jalur yang ditemukan adalah ``` ['A', 'B', 'D', 'G'] ```, karena DFS menyusuri jalur terdalam terlebih dahulu.

# BFS
Kode di atas mengimplementasikan algoritma Breadth-First Search (BFS) untuk mencari jalur dari node awal (start) ke node tujuan (goal) dalam sebuah graph yang direpresentasikan sebagai dictionary. Berikut adalah penjelasan fungsional dari setiap bagian kode:

1. Import Modul
  ```python
  from collections import deque
```
- ``` deque ``` dari modul ``` collections ``` digunakan untuk membuat queue (antrian) yang efisien untuk operasi enqueue dan dequeue.

2. Fungsi bfs(graph, start, goal)
   Fungsi ini melakukan pencarian jalur dari start ke goal menggunakan BFS.
   Inisialisasi
   ```python
   queue = deque([[start]])
   visited = set()
   ```
- ``` queue ``` menyimpan jalur yang sedang dieksplorasi, dimulai dengan jalur yang hanya berisi node awal (``` start ```).
- ``` visited ``` adalah set yang digunakan untuk melacak node yang telah dikunjungi agar tidak dikunjungi ulang.
  
Iterasi BFS
```python
while queue:
    path = queue.popleft()  
    node = path[-1]
    print("Visiting:", node)
```
- Loop berjalan selama masih ada jalur dalam ``` queue ```.
- Mengambil jalur pertama dari ``` queue ``` (``` path ```).
- Node terakhir dalam jalur (``` node ```) diambil untuk diperiksa.
  
Pengecekan Apakah Sudah Sampai di Tujuan
```python
if node == goal:
    return path
```
- Jika ``` node ``` adalah node tujuan (``` goal ```), maka jalur (``` path ```) dikembalikan.
  
Menambahkan Tetangga ke dalam Queue
```python
if node not in visited:
    visited.add(node)
    for neighbor in graph.get(node, []):
        new_path = list(path)
        new_path.append(neighbor)
        queue.append(new_path)
```
- Jika ``` node ``` belum dikunjungi, maka ditambahkan ke ``` visited ```.
- Semua tetangga (``` neighbor ```) dari node yang belum dikunjungi diambil dari ``` graph ```.
- Membuat jalur baru (``` new_path ```) dengan menambahkan ``` neighbor ``` ke jalur saat ini.
- Jalur baru dimasukkan ke dalam ``` queue ``` untuk eksplorasi selanjutnya.

Jika Tidak Ditemukan Jalur
```python
return None
```
- Jika semua node telah dieksplorasi dan goal tidak ditemukan, fungsi mengembalikan ``` None ```.

3.  Bagian Main Program
```python
if __name__ == "__main__":
```
Kode ini memastikan bahwa bagian di bawahnya hanya dijalankan jika skrip dieksekusi secara langsung, bukan diimpor sebagai modul.

Definisi Graph
```python
example_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}
```
- Graph direpresentasikan sebagai dictionary di mana key adalah node dan value adalah daftar tetangganya.
  
Menjalankan BFS
```python
print("BFS Path:", bfs(example_graph, 'A', 'G'))
```
- Memanggil fungsi ``` bfs ``` untuk mencari jalur dari ``` 'A' ``` ke ``` 'G' ```.
- Hasil jalur akan dicetak.

Contoh Eksekusi
Jika dijalankan, program akan mencetak urutan node yang dikunjungi dan jalur hasil BFS:
```pgsql
Visiting: A
Visiting: B
Visiting: C
Visiting: D
Visiting: E
Visiting: F
Visiting: G
BFS Path: ['A', 'B', 'D', 'G']
```
- Jalur yang ditemukan adalah ``` ['A', 'B', 'D', 'G'] ```, yang merupakan jalur pertama yang ditemukan oleh BFS.

# UCS
Kode di atas mengimplementasikan algoritma Uniform Cost Search (UCS) untuk mencari jalur dengan biaya minimum dari node awal (start) ke node tujuan (goal) dalam graph berbobot. UCS mirip dengan BFS tetapi mempertimbangkan biaya (cost) untuk mencapai setiap node.

1. Import Library yang Diperlukan
```python
import heapq
```
- ``` heapq ``` digunakan untuk mengelola priority queue berbasis heap min yang memastikan jalur dengan biaya terendah diproses lebih dulu.
  
2. Definisi Fungsi UCS
```python
def ucs(graph, start, goal):
```
- ``` graph ``` → Representasi graph dalam bentuk dictionary dengan edge berbobot.
- ``` start ``` → Node awal pencarian.
- ``` goal ``` → Node tujuan.
  
3. Inisialisasi Priority Queue dan Visited Set
```python
priority_queue = [(0, [start])]
visited = set()
```
- ```priority_queue ``` menyimpan (cost, path) dan diinisialisasi dengan cost 0 serta jalur yang hanya berisi node start.
- ``` visited ``` adalah set untuk melacak node yang sudah dikunjungi, menghindari eksplorasi ulang.

4. Looping UCS
```python
while priority_queue:
    cost, path = heapq.heappop(priority_queue)
    node = path[-1]
    print("Visiting:", node, "with cost:", cost)
```
- Loop berjalan selama masih ada jalur yang harus diperiksa.
- Ambil jalur dengan biaya terkecil dari ``` priority_queue ``` menggunakan ``` heapq.heappop() ```.
- ``` node = path[-1] ``` → Node terakhir dari jalur saat ini diambil untuk diperiksa.

5. Pengecekan Apakah Sudah Sampai di Tujuan
```python
if node == goal:
    return path, cost
```
- Jika ``` node ``` adalah ``` goal ```, mengembalikan jalur beserta biaya total.

6. Menambahkan Tetangga ke Priority Queue
```python
if node not in visited:
    visited.add(node)
    for neighbor, weight in graph.get(node, []):
        new_path = list(path)
        new_path.append(neighbor)
        heapq.heappush(priority_queue, (cost + weight, new_path))
```
- Jika ``` node ``` belum dikunjungi, tambahkan ke ``` visited ```.
- Iterasi semua tetangga (``` neighbor ```) beserta bobot (``` weight ```).
- Buat jalur baru (``` new_path ```) dengan menambahkan ``` neighbor ```.
- Tambahkan jalur baru ke ``` priority_queue ```, dengan biaya total diperbarui (``` cost + weight ```).
  
7. Jika Tidak Ditemukan Jalur
```python
return None, float('inf')
```
- Jika tidak ada jalur menuju ``` goal ```, mengembalikan ``` None ``` dan biaya ``` inf ``` (tak terhingga).
  
8. Bagian Main Program
```python
if __name__ == "__main__":
```
- Memastikan kode di bawahnya hanya dieksekusi jika skrip dijalankan langsung.
  
Membuat Graph Berbobot
```python
example_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}
```
- Graph direpresentasikan sebagai dictionary di mana key adalah node dan value adalah list tuple berisi tetangga dan bobotnya.

Menjalankan UCS
```python
path, cost = ucs(example_graph, 'A', 'G')
print("UCS Path:", path, "with minimum cost:", cost)
```
- Mencari jalur dengan biaya minimum dari ``` 'A' ``` ke ``` 'G' ``` menggunakan UCS.
- Menampilkan hasil jalur dan biaya totalnya.
  
Contoh Eksekusi
Jika dijalankan, program akan mencetak jalur yang dikunjungi dan hasil UCS:

```pgsql
Visiting: A with cost: 0
Visiting: B with cost: 1
Visiting: D with cost: 3
Visiting: G with cost: 4
UCS Path: ['A', 'B', 'D', 'G'] with minimum cost: 4
```
Penjelasan jalur yang ditemukan (``` ['A', 'B', 'D', 'G'] ``` dengan biaya ``` 4 ```):

- A → B (1)
- B → D (2) → Total biaya ``` 1 + 2 = 3 ```
- D → G (1) → Total biaya ``` 3 + 1 = 4 ```
  
UCS memilih jalur dengan total biaya paling rendah, bukan sekadar jalur dengan paling sedikit node.




