import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Data Titik Akses: label -> (x, y)
titik_akses = {
    'A': (1, 2),
    'B': (2, 5),
    'C': (5, 3),
    'D': (6, 7),
    'E': (3, 1)
}

# Membuat graf dan menambahkan node dengan posisi yang sudah didefinisikan
G = nx.Graph()
for label, koordinat in titik_akses.items():
    G.add_node(label, pos=koordinat)

# Fungsi untuk menghitung jarak Euclidean antara dua titik menggunakan NumPy
def jarak_euclidean(p, q):
    p = np.array(p)
    q = np.array(q)
    return np.linalg.norm(p - q)

# Menambahkan semua sisi antar titik dengan bobot berupa jarak Euclidean
daftar_label = list(titik_akses.keys())
for i in range(len(daftar_label)):
    for j in range(i+1, len(daftar_label)):
        jarak = jarak_euclidean(titik_akses[daftar_label[i]], titik_akses[daftar_label[j]])
        G.add_edge(daftar_label[i], daftar_label[j], weight=jarak)

# Mencari jalur terpendek dari titik 'A' ke 'D' menggunakan algoritma Dijkstra
sumber, tujuan = 'A', 'D'
jalur_terpendek = nx.dijkstra_path(G, source=sumber, target=tujuan, weight='weight')
print("Jalur terpendek dari {} ke {}: {}".format(sumber, tujuan, jalur_terpendek))

# Visualisasi graf dan sorot jalur terpendek
posisi = nx.get_node_attributes(G, 'pos')
nx.draw(G, posisi, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500)

# Tandai sisi-sisi yang ada di jalur terpendek dengan warna merah
sisi_jalur = list(zip(jalur_terpendek, jalur_terpendek[1:]))
nx.draw_networkx_edges(G, posisi, edgelist=sisi_jalur, edge_color='red', width=2)

plt.title("Graf Titik Akses Wi-Fi & Jalur Terpendek")
plt.show()