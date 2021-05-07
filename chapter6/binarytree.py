class BinaryTree:
    def __init__(self, rootObj) -> None:
        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, obj):
        if self.left == None:
            self.left = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.left = self.left
            self.left = t

    def insertRight(self, obj):
        if self.right == None:
            self.right = BinaryTree(obj)
        else:
            t = BinaryTree(obj)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key
