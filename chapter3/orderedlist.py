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


class OrderedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, item):
        if self.isEmpty():
            self.head = Node(item)
            return
        current = self.head
        previous = None
        while current != None:
            if current.getData() < item:
                previous = current
                current = current.getNext()
            else:
                break
        temp = Node(item)
        temp.setNext(current)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

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
        found = False
        while current != None:
            if current.getData() < item:
                current = current.getNext()
            elif current.getData() == item:
                found = True
                break
            else:
                break
        return found

    def isEmpty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def index(self, item):
        pos = 0
        current = self.head
        while current != None:
            if current.getData() < item:
                current = current.getNext()
                pos = pos+1
            elif current.getData() > item:
                raise Exception('Not in list')
            else:
                return pos

    def pop(self, pos=None):
        if pos == None:
            return self.__popLast()
        if pos == 0:
            self.head.setNext(self.head.getNext())
        else:
            index = 0
            current = self.head
            previous = None

            while index < pos:
                previous = current
                current = current.getNext()
                index = index + 1
            previous.setNext(current.getNext())

    def __popLast(self):
        current = self.head
        if current.getNext() == None:
            self.head = None
            return
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        previous.setNext(None)
