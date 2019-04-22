# -*- coding:utf-8 -*-
'''
    数据流中的中位数
======================
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有
数值排序后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值
排序后位于中间两个数的平均值。
'''

import heapq
def streamMedian():
    '''
    思路：可以把数据流看成由两个部分组成的数组，数组之间的长度之差不超过1，
    且左边的数组长度大于等于右边的数组长度，左边部分的数据都比右边数据要小。
    所以当两个数组长度相等时，中位数就是各自最大值之和的平均值；当不相等是，
    中位数是左边数组的最大值。从以上的描述可以看出，该思路可以用一个最大堆
    和一个最小堆实现，左边数组维护一个最大堆，右边数组维护一个最小堆。
    '''
    maxHeap = []
    minHeap = []
    while True:
        x = input('please input a number or a space to stop: ')
        if x == ' ':
            if len(maxHeap) == 0 and len(minHeap) == 0:
                return

            if (len(maxHeap) + len(minHeap)) & 1 == 0:
                res = (maxHeap[0] - minHeap[0]) / 2
            else:
                res = maxHeap[0]
            print('数据流中位数: ', res)
            return res

        x = float(x)
        if (len(maxHeap) + len(minHeap)) & 1 == 0:
            if len(minHeap) > 0:
                heapq.heappush(minHeap, -x)
                x = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -x)
        else:
            if len(maxHeap) > 0:
                heapq.heappush(maxHeap, x)
                x = -1 * heapq.heappop(maxHeap)
            heapq.heappush(minHeap, x)


if __name__ == '__main__':
    streamMedian()