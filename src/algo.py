
def mergeSortedArrays(arr1, arr2):
    if arr1 is None and arr2 is None:
        return []
    if arr1 is None and arr2 is not None:
        return arr2
    aptr = 0
    bptr = 0
    result = []
    while aptr < len(arr1) and bptr < len(arr2):
        if arr1[aptr] < arr2[bptr]:
            result.append(arr1[aptr])
            aptr += 1
        else:
            result.append(arr2[bptr])
            bptr += 1
    return result


if __name__ == "__main__":
    print(mergeSortedArrays([1, 2, 7, 8], [3, 4, 7]))
