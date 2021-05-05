def binarySearch(alist, item):
    found = False
    subList = alist
    while len(subList) > 0 and not found:
        length = len(subList)
        mid = length // 2
        if subList[mid] > item:
            subList = subList[:mid]
        elif subList[mid] < item:
            subList = subList[mid+1:]
        else:
            found = True
    return found
