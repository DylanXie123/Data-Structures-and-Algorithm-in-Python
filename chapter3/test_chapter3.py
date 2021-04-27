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
