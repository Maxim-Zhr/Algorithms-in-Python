import random
def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[random.randint(0, len(array)-1)]
    less = [s for s in array if s < pivot]
    greater = [s for s in array if s > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)



print(quicksort([1, 3, 5, 2, 4]))