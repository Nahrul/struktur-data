# inisiasi class stacks
class Stacks:
    def __init__(self):
        # inisiasi variabel menjadi stacks
        self.items = []

    #implementasi push (menambahkan data ke dalam stacks)
    def push(self, item):
        self.items.append(item)

    #implementasi isempty(cek stack kosong/ tidak)
    def isEmpty(self):
        # jika items == 0 maka tampilkan stack kosong
        if(len(self.items)==0):
            print("stack Kosong")
        # jika stack items ada isi nya maka tampilkan
        print(f"isi stacks: {self.items}")

        # implementasi konsep pop (mengambil/menghapus elemen)
    def pop(self):
        # jika items tidak == 0 maka hapus menggunakan pop
        if not len(self.items)==0:
            return self.items.pop()
        # jika stacks kosong maka tampilkan text stacks kosong
        return "Stacks Kosong"
    

    #implementasi top (untuk melihat tumpukan teratas)
    def top(self):
        # tampilkan items paling atas dengan index 0
        print(self.items[-1])

#penggunaan class dan function

myTumpuk = Stacks()
myTumpuk.push("Page 1")
myTumpuk.push("Page 2")
myTumpuk.push("Page 3")
myTumpuk.isEmpty()
myTumpuk.pop()
myTumpuk.isEmpty()
myTumpuk.top()