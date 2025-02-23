#tugas uts Bagian 3 Soal no 2:Mencari Nilai x(300) dalam Himpunan A
#DIketahui :
#Himpunan
A = [ 109, 222, 120, 150, 200, 321, 410, 120, 230, 300, 111, 89, 70, 45, 57, 31, 39, 900, 21,
378, 400, 101, 201, 301, 1]
def mencari(tugas, x):
    for i in range(len(tugas)):
        if tugas[i] == x:
            return i  
        
# Mencari Nilai x (300)
x = 300
urutan = mencari(A, x)
if urutan:
    print(f"Selamat Nilai {x} akhirnya telah ditemukan pada urutan ke-{urutan + 1}.")
else:
    print(f"Nilai {x} sayangnya tidak ditemukan dalam himpunan A.")
    
    