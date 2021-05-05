def shellSort(alist):
    subListCount = len(alist) // 2
    while subListCount > 0:
        for startPos in range(subListCount):
            gapInsertSort(alist, startPos, subListCount)
        subListCount = subListCount // 2


def gapInsertSort(alist, startPos, gap):
    n = len(alist)
    for i in range(startPos, n-gap, gap):
        value = alist[i+gap]
        index = startPos
        for j in range(i, startPos-1, -gap):
            if alist[j] > value:
                alist[j+gap] = alist[j]
            else:
                index = j + gap
                break
        alist[index] = value
