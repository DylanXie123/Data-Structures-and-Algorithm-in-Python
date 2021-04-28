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
        pass

    def search(self, item):
        current = self.head
        while current != None:
            if current.getData() != item:
                current = current.getNext()
            else:
                return True
        return False

    def append(self, item):
        pass

    def index(self, item):
        current = self.head
        pos = 0
        while current != None:
            if current.getData() != item:
                pos = pos + 1
                current = current.getNext()
        return pos

    def insert(self, pos, item):
        pass

    def pop(self):
        pass

    def pop(self, pos):
        pass
