# Buatlah sebuah Aplikasi To Do list  dengan bahasa Python dengan prinsip - prinsip Linkedlist

# yang memuat Menu:

# Menambah List
# Menambah List dari depan
# Menampilkan List berdasar index
# Menghapus List dari depan
# Menghapus List dari belakang
# Menghapus List berdasar lokasi Index
# Mengecek Jumlah To do List
# Menu Exit
# Menu jika pilihan tidak ada

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class TodoList:
    def __init__(self):
        self.head = None

    def AddLast(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print("To Do List Berhasil ditambahkan di belakang!")

    def AddFirst(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("To Do List berhasil ditambahkan di depan!")

    def ShowByIndex(self, index):
        current = self.head
        i = 0
        while current:
            if i == index:
                print(f"Data pada index {index} adalah: {current.data}")
                return
            current = current.next
            i += 1
        print("Index tidak ditemukan!")

    def DeleteFirst(self):
        if not self.head:
            print("To Do List Kosong")
        else:
            print(f"List {self.head.data} dihapus dari depan")
            self.head = self.head.next
    
    def DeleteLast(self):
        if not self.head:
            print("To Do List Kosong!")
        elif not self.head.next:
            print(f"List {self.head.data} dihapus dari belakang")
            self.head = None
        else:
            prev = None
            current = self.head
            while current.next:
                prev = current
                current = current.next
            print(f"List {current.data} dihapus dari belakang")
            prev.next = None
    def DeleteByIndex(self, index):
        if not self.head:
            print("List kosong!")
            return
        if index == 0:
            print(f"List '{self.head.data} dihapus dari index 0")
            self.head = self.head.next
            return
        current = self.head
        prev = None
        i = 0
        while current and i != index:
            prev = current
            current = current.next
            i += 1
        if not current:
            print("Index tidak ditemukan!")
        else:
            print(f"List '{current.data}' dihapus dari index {index}")
            prev.next = current.next

    def jumlah(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print(f"Jumlah To Do List: {count}")
    
    def show(self):
        if not self.head:
            print("To Do List Kosong.")
        else:
            current = self.head
            i = 0
            while current:
                print(f"[{i}] {current.data}")
                current = current.next
                i += 1

def main():
    todo = TodoList()

    while True:
        print("\n=== MENU TO DO LIST (Linked List) ===")
        print("1. Menambah List dari belakang")
        print("2. Menambah List dari depan")
        print("3. Menampilkan List berdasarkan index")
        print("4. Menghapus List dari depan")
        print("5. Menghapus List dari belakang")
        print("6. Menghapus List berdasarkan index")
        print("7. Mengecek jumlah To Do List")
        print("8. Tampilkan semua To Do List")
        print("9. Keluar")
        pilihan = input("Pilih menu (1-9): ")

        if pilihan == '1':
            data = input("Masukkan data To Do: ")
            todo.AddLast(data)
        elif pilihan == '2':
            data = input("Masukkan data To Do: ")
            todo.AddFirst(data)
        elif pilihan == '3':
            idx = int(input("Masukkan index yang ingin ditampilkan: "))
            todo.ShowByIndex(idx)
        elif pilihan == '4':
            todo.DeleteFirst()
        elif pilihan == '5':
            todo.DeleteLast()
        elif pilihan == '6':
            idx = int(input("Masukkan index yang ingin dihapus: "))
            todo.DeleteByIndex(idx)
        elif pilihan == '7':
            todo.jumlah()
        elif pilihan == '8':
            todo.show()
        elif pilihan == '9':
            print("Terima kasih telah menggunakan To Do List!")
            break
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")

if __name__ == "__main__":
    main()


        
