from chapter5.quickSort import quickSort
from chapter5.mergeSort import mergeSort
from chapter5.shellSort import shellSort
from chapter5.insertSort import insertSort
from chapter5.selectionSort import selectionSort
from chapter5.bubbleSort import bubbleSort
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

def test_bubbleSort():
    a = [43, 45, 9, 88, 0]
    bubbleSort(a)
    assert a[0] == 0
    assert a[1] == 9
    assert a[2] == 43
    assert a[3] == 45
    assert a[4] == 88

def test_selectionSort():
    a = [43, 45, 9, 88, 0]
    selectionSort(a)
    assert a[0] == 0
    assert a[1] == 9
    assert a[2] == 43
    assert a[3] == 45
    assert a[4] == 88

def test_insertSort():
    a = [43, 45, 9, 88, 0]
    insertSort(a)
    assert a[0] == 0
    assert a[1] == 9
    assert a[2] == 43
    assert a[3] == 45
    assert a[4] == 88

def test_shellSort():
    a = [43, 45, 9, 88, 0]
    shellSort(a)
    assert a[0] == 0
    assert a[1] == 9
    assert a[2] == 43
    assert a[3] == 45
    assert a[4] == 88

def test_mergeSort():
    a = [43, 45, 9, 88, 0]
    mergeSort(a)
    assert a[0] == 0
    assert a[1] == 9
    assert a[2] == 43
    assert a[3] == 45
    assert a[4] == 88

def test_quickSort():
    a = [43, 45, 9, 88, 0]
    quickSort(a)
    assert a[0] == 0
    assert a[1] == 9
    assert a[2] == 43
    assert a[3] == 45
    assert a[4] == 88