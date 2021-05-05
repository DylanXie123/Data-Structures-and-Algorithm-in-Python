def insertSort(alist):
    n = len(alist)
    for i in range(n-1):
        value = alist[i+1]
        index = 0
        for j in range(i, -1, -1):
            if alist[j] > value:
                alist[j+1] = alist[j]
            else:
                index = j + 1
                break
        alist[index] = value
