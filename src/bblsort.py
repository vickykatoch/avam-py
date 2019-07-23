#! /usr/bin/env python

# Runtime complexity: O(n^2)


def bubbleSort(nums):
    ctr = 0
    for i in range(0, len(nums)-1):
        ctr += 1
        for j in range(i+1, len(nums)):
            ctr += 1
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return (nums, ctr)


if __name__ == "__main__":
    nums = bubbleSort([10, 15, 8, 5, 3])
    print('N : {0}, BigO: {1}'.format(len(nums[0]), nums[1]))
