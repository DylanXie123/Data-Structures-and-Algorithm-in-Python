from typing import Sized


class BinaryHeap:
    def __init__(self) -> None:
        self.heapList = [0]
        self.size = 0

    def insert(self, obj):
        self.heapList.append(obj)
        self.size = self.size + 1
        self.percUp()

    def percUp(self):
        index = self.size
        while index // 2 > 0:
            if self.heapList[index // 2] > self.heapList[index]:
                t = self.heapList[index]
                self.heapList[index] = self.heapList[index // 2]
                self.heapList[index // 2] = t
            index = index // 2

    def delMin(self):
        minItem = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.percDown(1)
        return minItem

    def percDown(self, i):
        while (i * 2) <= self.size:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        self.heapList = [0] + alist
        self.size = len(alist)
        i = self.size // 2
        while i > 0:
            self.percDown(i)
            i = i - 1
