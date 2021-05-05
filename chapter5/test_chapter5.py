from chapter5.hashTable import HashTable
from chapter5.binarySearch import binarySearch
from chapter5.sequentialSearch import sequentialSearch


def test_sequentialSearch():
    a = list(range(10))
    assert sequentialSearch(a, 5) == True
    assert sequentialSearch(a, 20) == False


def test_binarySearch():
    a = list(range(10))
    assert binarySearch(a, 5) == True
    assert binarySearch(a, 20) == False

    a = list(range(3))
    assert binarySearch(a, 1) == True
    assert binarySearch(a, 20) == False


def test_HashTable():
    a = HashTable()
    a[54] = 'cat'
    a[26] = 'dog'
    a[93] = 'lion'
    a[17] = 'tiger'
    a[77] = 'bird'
    a[31] = 'cow'
    a[44] = 'goat'
    a[55] = 'pig'
    a[20] = 'chilcken'
    assert a[26] == 'dog'
    assert a[22] == None
