import random

def partition(nums, start, end):
    if not isinstance(nums, list) or len(nums) <= 0 \
        or start < 0 or end >= len(nums):
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
    data = [0,-1,-8,10,11,5,6]
    quickSort(data, 0, 6)
    print(data)



