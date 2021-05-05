def sequentialSearch(alist, item):
    pos = 0
    length = len(alist)
    found = False
    while pos < length and not found:
        if(alist[pos] == item):
            found = True
        else:
            pos = pos + 1
    return found