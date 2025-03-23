# membuat struktur data tuple#

# contoh 1
data = ("budi",20, "Indormatika")
print(data)
data= ("andi", 19, "Informatika")
print(data)
# mengakses Tuple
print(f" ini adalah index ke 0 {data[0]}")
print(f" ini adalah index ke -1 {data[-1]}")
# Tuple tidak bisa menerima tembahan elemen
#data.append("mahardika")

# tuple bisa di copy dan di duplicate
dataWarna = ("merah","biru","hijau","hitam")
dataWarna1 = dataWarna[0:2]
dataWarna3 = dataWarna [:]
print(dataWarna1)
print(dataWarna3)

#tuple bisa inisiasi ke variabel 
kotakMerah, KotakBiru, KotakHijau, kotakHitam = dataWarna
print(f"isi kotak merah adalah {kotakMerah}")

# apa benar strukdat list dan tuple menerima data
# sama sedangkan set tidak menerima 

List = ["andi","dika"]
Tuple = ("andi","andi")
Set = {"andi", "andi"}
print(List, Tuple, Set)
ubahSet = set(List)
set2 = set()
print(type(set2))
print(type(ubahSet))
print(ubahSet)
# set tidak bisa diakses menggunakan index
#print(ubahSet[0])
# menghapus data di set
ubahSet.discard("andi")
print(ubahSet)
ubahSet.remove("dika")
print(ubahSet)
# menambhakan anggota set
ubahSet.add("dika")
print(ubahSet)
ubahSet.update(["andi","caca"])
print(ubahSet)

# teknik rubah set
mySet = {1,2,3,4,5,6,7,8}
mySet.remove(4)
print(mySet)
mySet.add(10)
print(mySet)

# operasi pada set
#union
setA = {1,2,3,4,}
setB = {3,4,5,6}
setUnion = setA | setB
print(setUnion)
#intersection 
setIntersect = setA & setB
print(setIntersect)
# difference
setDiff = setB - setA
print(setDiff)
#symmetric difference
setSymDiff = setA ^ setB
print(setSymDiff)

#struktur data dictionary
dataMhs = [{
  "nama":"Budi",
   "NIM":1902,
   "Prodi":"Teknik informatika",
},
   {"nama":"Andi", 
   "NIM":1903, 
   "Prodi":"Teknik informatika"}]
#print(dataMhs)
#print(dataMhs[1]["nama"])
no = 0 
for c in dataMhs:
    no += 1
    print(no,f"Nama = {c['nama']} NIM = {c['NIM']} Prodi = {c['Prodi']}")
# merubah elemen dictionary

dataMhs[0]["nim"] = "Teknik Informatika"
print(dataMhs)