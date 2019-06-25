'''
        Median of Two Sorted Arrays
==========================================
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''


def findMedianSortedArrays(nums1: List[int], nums2: List[int]):
    def findKth(a, b, k):
        # 如果a为空的话，之间返回b中的第k小的元素
        if not a:
            return b[k]
        if not b:
            return a[k]

        mid_a = len(a) // 2
        mid_b = len(b) // 2
        if mid_a + mid_b < k:
            #说明 k 在mid_a + mid_b之外，所以k需要减去排除的那一部分的长度
            if a[mid_a] > b[mid_b]:
                return findKth(a, b[mid_b + 1:], k - mid_b - 1)
            else:
                return findKth(a[mid_a + 1:], b, k - mid_a - 1)
        else:
            #说明k在mid_a + mid_b之内，所以k不需要改变
            if a[mid_a] > b[mid_b]:
                return findKth(a[:mid_a], b, k)
            else:
                return findKth(a, b[:mid_b], k)

    if not isinstance(nums1, list) or not isinstance(nums2, list):
        return

    length = len(nums1) + len(nums2)
    if length & 1 == 1:
        return float(findKth(nums1, nums2, length // 2))
    else:
        return (findKth(nums1, nums2, length // 2)
                + findKth(nums1, nums2, length // 2 - 1)) / 2.0
