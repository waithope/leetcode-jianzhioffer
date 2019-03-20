'''
    邻值查询
================
有一个长度为n的序列A，A中的数各不相同。对于A中的每一个数Ai，求：
min(|Ai - Aj|), 1 <= j <= i
以及令上式取到最小值的j(记为Pi)。若最小值点不唯一，则选择使Aj较小的那个。
其中：
n <= 100000,
|Ai| <= 10e9

输入：长度n，以及序列nums
输出：n-1行，分别当i取2~n时，对应的min(|Ai - Aj|), 1 <= j <= i 和 Pi
'''


class Node(object):
    def __init__(self, pos=-1, val=-1, prev=-1, nxt=-1):
        self.pos = pos
        self.val = val
        self.prev = prev
        self.next = nxt

def findMinimum(n, nums):
    '''
    提示：先将序列nums以及其对应的下标组合，并按序列值进行排序，接着创建一个链表，
    将排序后的序列值以及对应的原始下标存入链表节点中，并用一个数组保存节点编号（节点编号存入
    该序列值对应的原始下标的位置，方便后续直接定位节点位置，而不用一个一个遍历），最后
    根据原始序列从后向前遍历，每读取一个序列值，找到其在链表中的位置，分别计算其值
    与前后节点值的差的绝对值res1, 和res2。

    时间O(nlgn)+O(n), 空间O(n)
    '''
    if not isinstance(n, int) or n <= 0 or n > 100000:
        return
    if not isinstance(nums, list) or len(nums) <=0 or n != len(nums):
        return

    global tail
    tail = -1
    nodes = [Node() for i in range(n)]

    def insertNode(pos, val):
        global tail
        tail += 1
        nodes[tail].pos = pos
        nodes[tail].val = val
        nodes[tail].prev = tail-1
        nodes[tail-1].next = tail

    def removeNode(p):
        nodes[p].pos = -1
        nodes[nodes[p].prev].next = nodes[p].next
        nodes[nodes[p].next].prev = nodes[p].prev

    # 将序列下标值与序列一对一组合，并以序列值大小排序
    sortedNums = sorted(map(list, zip([i for i in range(n)], nums)), key=lambda x: x[1])
    pointerToNode = [-1] * n
    tail += 1
    nodes[tail].pos = sortedNums[0][0]
    nodes[tail].val = sortedNums[0][1]
    pointerToNode[sortedNums[0][0]] = tail
    for i in range(1, n):
        insertNode(sortedNums[i][0], sortedNums[i][1])
        pointerToNode[sortedNums[i][0]] = tail

    for i in range(n-1, 0, -1):
        res1 = res2 = 2*32
        if nodes[pointerToNode[i]].prev != -1:
            res1 = abs(nums[i] - nodes[nodes[pointerToNode[i]].prev].val)
        if nodes[pointerToNode[i]].next != -1:
            res2 = abs(nums[i] - nodes[nodes[pointerToNode[i]].next].val)
        if res1 <= res2:
            sortedNums[i][0] = res1
            sortedNums[i][1] = nodes[nodes[pointerToNode[i]].prev].pos + 1
        else:
            sortedNums[i][0] = res2
            sortedNums[i][1] = nodes[nodes[pointerToNode[i]].next].pos + 1
        removeNode(pointerToNode[i])     # 删除当前pos所对应的节点

    for i in range(1, n):
        print(' '.join((map(str, sortedNums[i]))))

print('测试用例1：')
findMinimum(3, [1, 5, 3])
print('测试用例2：')
findMinimum(6, [1, 5, 3, 8, 2, 10])
