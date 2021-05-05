def selectionSort(alist):
    n = len(alist)
    for i in range(n):
        max = 0
        for j in range(n-i):
            if alist[j] > alist[max]:
                max = j
        temp = alist[n-i-1]
        alist[n-i-1] = alist[max]
        alist[max] = temp
