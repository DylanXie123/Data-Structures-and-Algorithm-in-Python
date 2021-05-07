from chapter3.stack import Stack
from chapter6.binarytree import BinaryTree


def buildParseTree(expStr):
    strList = expStr.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for str in strList:
        if str == '(':
            eTree.insertLeft('')
            currentTree = eTree.left
            pStack.push(currentTree)
        elif str in '+-/*':
            currentTree.setRootVal(str)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif str in ')':
            currentTree = pStack.pop()
        else:
            currentTree.setRootVal(eval(str))
            currentTree = pStack.pop()
    return eTree


opers = {
    '-': lambda a, b: a + b,
    '+': lambda a, b: a + b,
    '*': lambda a, b: a + b,
    '/': lambda a, b: a + b,
}


def evaluate(tree: BinaryTree):
    if tree.getLeftChild() == None and tree.getRightChild() == None:
        return tree.getRootVal()
    else:
        fn = opers[tree.getRootVal()]
        return fn(evaluate(tree.getLeftChild()), evaluate(tree.getRightChild()))
