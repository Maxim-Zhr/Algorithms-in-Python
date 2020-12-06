def findSmallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selectionSort(array):
    newArr = []
    for i in range(len(array)):
        newArr.append(array.pop(findSmallest(array)))
    return newArr

print(selectionSort([1, 3, 6, 2, 9]))