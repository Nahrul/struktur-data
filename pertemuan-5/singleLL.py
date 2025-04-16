myList = ["Orange", "Yellow", "Green", "Red", "Blue"]
print(myList)

# Membuat Single Linked List
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def inser_at(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.insertAtBeginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return
    def removeAt(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        return
    

if __name__ == "__main__":
    mySll = SingleLinkedList()
    mySll.inser_at(0, "Apple")
    mySll.inser_at(1, "Mango")
    mySll.inser_at(2, "Banana")
    mySll.printList()

    mySll.insertAtBeginning("Orange")
    mySll.printList()

    mySll.insertAtEnd("Watermelon")
    mySll.printList()
    mySll.removeAt(2)
    mySll.printList()