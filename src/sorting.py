
def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            temp = array[j-1]
            array[j-1] = array[j]
            array[j] = temp
            j -= 1
    return array


def bubbleSort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-1):
            if(array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array

# [3, 2, 6, 34, 12, 3]


def selectionSort(array):
    for i in range(0, len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[min] > array[j]):
                min = j
        if min != i:
            temp = array[i]
            array[i] = array[min]
            array[min] = temp
    return array


if __name__ == "__main__":
    print(insertionSort([3, 2, 6, 34, 12, 3, 6, 3, 15, 20, 30, 1, 5, 7]))
    print(bubbleSort([3, 2, 6, 34, 12, 3, 6, 3, 15, 20, 30, 1, 5, 7]))
    print(selectionSort([3, 2, 6, 34, 12, 3, 6, 3, 15, 20, 30, 1, 5, 7]))
