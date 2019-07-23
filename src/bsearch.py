import math
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 30, 40, 50,
         63, 64, 66, 78, 81, 89, 90, 92, 93, 95, 100]
min = 0
max = len(items)
ctr = 0
index = -1
target = 63

while min < max:
    mid = int(round((min+max)/2, 0))
    ctr += 1
    if items[mid] == target:
        index = mid
        break
    elif target > items[mid]:
        min = mid+1
    elif target < items[mid]:
        max = mid-1
if index >= 0:
    print('Item found at index : {0} in {1}th iterations'.format(index, ctr))
else:
    print('Item not found, iterations : {0}'.format(ctr))
