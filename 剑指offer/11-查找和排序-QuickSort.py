import random

def partition(nums, start, end):
    if (not isinstance(nums, list) or len(nums) <= 0
        or start < 0 or end >= len(nums)):
        return -1

    index = random.randint(start, end)
    nums[index], nums[end] = nums[end], nums[index]
    small = start - 1
    for i in range(start, end+1):
        if nums[i] < nums[end]:
            small += 1
            if small != i:
                nums[small], nums[i] = nums[i], nums[small]

    small += 1
    nums[small], nums[end] = nums[end], nums[small]
    return small

def quickSort(nums, start, end):
    if start == end:
        return

    index = partition(nums, start, end)

    if index > start:
        quickSort(nums, start, index - 1)
    if index < end:
        quickSort(nums, index + 1, end)



if __name__ == '__main__':
    # test1
    data1 = [0,-1,-8,10,11,5,6]
    quickSort(data1, 0, len(data1)-1)
    assert(data1 == [-8,-1,0,5,6,10,11])
    # test2
    data2 = [5,4,3,2,1,0,-1,-2]
    quickSort(data2, 0, len(data2)-1)
    assert(data2 == [-2,-1,0,1,2,3,4,5])
    # test3
    data3 = [1,1,1,2,2,2,0,0,0,-1,-1,-1]
    quickSort(data3, 0, len(data3)-1)
    assert(data3 == [-1,-1,-1,0,0,0,1,1,1,2,2,2])
    # test4
    data4 = [13,4,12,1,14,11,7,3,9,10,5,2,6,8]
    quickSort(data4, 0, len(data4)-1)
    assert(data4 == [1,2,3,4,5,6,7,8,9,10,11,12,13,14])



