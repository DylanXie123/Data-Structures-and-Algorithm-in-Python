from chapter6.binarytree import BinaryTree


def test_binaryTree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    assert t.getLeftChild().getRootVal() == 'b'
    assert t.getRightChild().getRootVal() == 'c'
    assert t.getRootVal() == 'a'
