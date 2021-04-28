class Node:
    def __init__(self, initData) -> None:
        self.data = initData
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class UnorderedList:
    def __init__(self) -> None:
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        newNode = Node(item)
        newNode.setNext(self.head)
        self.head = newNode

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        while current != None:
            if current.getData() != item:
                previous = current
                current = current.getNext()
            else:
                if previous == None:
                    self.head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                return

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() != item:
                current = current.getNext()
            else:
                return True
        return False

    def append(self, item):
        current = self.head
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(Node(item))

    def index(self, item):
        current = self.head
        pos = 0
        while current != None:
            if current.getData() != item:
                pos = pos + 1
                current = current.getNext()
            else:
                return pos

    def insert(self, pos, item):
        pass

    def pop(self):
        pass

    def pop(self, pos):
        pass
