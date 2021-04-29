from chapter3.unorderedlist import UnorderedList
from chapter3.deque import Deque
from chapter3.queue import Queue
from chapter3.stack import Stack


def test_stack():
    s = Stack()
    assert s.isEmpty() == True
    s.push(1)
    s.push(10)
    s.push('hello')
    s.push(0.5)
    assert s.isEmpty() == False
    assert s.size() == 4
    assert s.peek() == 0.5
    s.pop()
    assert s.peek() == 'hello'


def test_queue():
    q = Queue()
    assert q.isEmpty() == True
    q.enqueue(1)
    q.enqueue('dog')
    q.enqueue(0.5)
    assert q.isEmpty() == False
    assert q.size() == 3
    assert q.dequeue() == 1
    assert q.dequeue() == 'dog'
    assert q.dequeue() == 0.5


def test_deque():
    d = Deque()
    assert d.isEmpty() == True
    d.addFront(1)
    d.addFront('dog')
    d.addRear(0.5)
    d.addRear(10)
    assert d.isEmpty() == False
    assert d.size() == 4
    assert d.removeFront() == 'dog'
    assert d.removeRear() == 10


def test_unorderedList():
    l = UnorderedList()
    assert l.isEmpty() == True
    assert l.size() == 0 
    l.add(2)
    l.add('0.5')
    assert l.size() == 2
    assert l.search(2) == True
    assert l.search('0.5') == True
    assert l.search(4) == False
    assert l.index(2) == 1
    assert l.index('0.5') == 0
    l.add(10)
    l.add(9)
    assert l.search(10) == True
    assert l.search(9) == True
    l.remove(10)
    l.remove(9)
    assert l.search(10) == False
    assert l.search(9) == False
    l.append(4)
    assert l.size() == 3
    assert l.index(4) == 2
    l.insert(1, 10)
    assert l.size() == 4
    assert l.index(10) == 1
    assert l.index('0.5') == 0
    assert l.index(2) == 2
    l.pop()
    assert l.size() == 3
    assert l.search(4) == False
    l.pop(1)
    assert l.size() == 2
    assert l.search(10) == False
