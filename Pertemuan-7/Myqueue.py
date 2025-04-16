class Myqueue:
    def __init__(self):
        self.items = []
    
    # fungsi enqueue eppend
    def enQueue(self, item):
        self.items.append(item)

    # fungsi deQueue POP
    def deQueue(self):
        return self.items.pop(0)

    # fungsi isempty untuk menghapus semua item
    def isEmpty(self):
        return len(self.items) == 0
    
    # fungsi front untuk mengecek antrian terdepan
    def front(self):
        return self.items[0]
    
    # fungsi show untuk menampilkan semua items
    def show(self):
        print(self.items)


# inisiasi class class ke variabel
queue = Myqueue()
# menghapus semua antrian
print(queue.isEmpty())

# mengisi antrian
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)

# tampilkan antrian
queue.show()

# tampilkan antrian terdepan
print(f"antrian terdepan adalah {queue.front()}")

# hapus antrian terdepan
queue.deQueue()

# tampilkan antrian terdepan
print(f"antrian terdepan adalah: {queue.front()}")