from chapter6.binaryheap import BinaryHeap
from chapter6.buildParserTree import buildParseTree, evaluate
from chapter6.binarytree import BinaryTree


def test_binaryTree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    assert t.getLeftChild().getRootVal() == 'b'
    assert t.getRightChild().getRootVal() == 'c'
    assert t.getRootVal() == 'a'

def test_parseTree():
    exp = '(3+(4*5))'
    tree = buildParseTree(exp)
    assert evaluate(tree) == 23

def test_binaryHeap():
    heap = BinaryHeap()
    heap.buildHeap([9, 6, 5, 2, 3])
    heap.insert(1)
    assert heap.delMin() == 1
    assert heap.delMin() == 2