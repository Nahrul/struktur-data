# Membuat List
myList =["Mahardika",  1, True, 4.6]
 #List bersigfat mutable / indexing
# untuk menampilkan isi list index 0
print(myList[0])
print(myList[-4])

# sifat slicing
# menampilkan index ke 1 sampai 3
print(myList[0:4])

print(f"mencetak dari index awal sampai ke index 2 {myList[:3]}")
dataMhs = [{"nama":"Budi", "NIM":1902, "Prodi":"Teknik informatika"},
           {"nama":"Andi", "NIM":1903, "Prodi":"Teknik informatika"},
           {"nama":"caca", "NIM":1904, "Prodi":"Teknik informatika"}]
no=0
# menampilkan list berdasarkan index
for i in dataMhs:
    no=no+1
    print(f"{no}.Nama = {i['nama']} Nim = {i['NIM']} Prodi = {i['Prodi']}")

# sifat merubah isi List
myList[0] = "Informatika"
myList[3] = "empat koma enam"
print(myList)

# menghitung jumlah data dalam list
print(len(dataMhs))
# menambhakn elemen pada list
myList.insert(0, "Mahardika")
print(f"menambahkan Mahardika didepan {myList}")
# menambahkan elemen pada list langsung di belakang
myList.append("Kampus")
print(f" setelah ditambhkan append jadi ada kampus di belakang {myList}")
# menghapus elemen pada list
myList.remove("Mahardika")
print(f"setelah dihapus menggunakan remove{myList}")
myList.pop(2)
print(myList)

# mengurutkan list,
listWarna = ["merah","biru","hijau","kuning"]
listWarna.sort
print(listWarna)
listWarna.reverse()
print(listWarna)
# menjumlahkan isi list
listAngka = [1,2,3,4,5,6]
print(sum(listAngka))
#membuat salinan dengan copy
b = listWarna.copy()
print(b)