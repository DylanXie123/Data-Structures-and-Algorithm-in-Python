def bubbleSort(alist):
    n = len(alist)
    for i in range(n):
        for j in range(n-i-1):
            if alist[j] > alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
