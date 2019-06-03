# -*- coding:utf-8 -*-
'''
        队列的最大值
============================
请定义一个队列并实现函数max得到队列的最大值，要求函数max、push_back和pop_front
的时间复杂度都是O(1)。
'''

from collections import deque
class QueueWithMax(object):
    '''
    思路：借助59-01-滑动窗口的最大值的思想，用两个双端队列来实现带max函数的队列。
    其中，一个队列保存数字，另一个队列保存数字队列的当前最大值。
    '''
    def __init__(self):
        self.queue = deque()
        self.maxInQueue = deque()
        self.index = 0
    def push_back(self, num):
        while len(self.maxInQueue) != 0 and num > self.maxInQueue[-1][1]:
            self.maxInQueue.pop()
        self.queue.append([self.index, num])
        self.maxInQueue.append([self.index, num])
        self.index += 1
    def pop_front(self):
        if len(self.queue) == 0:
            raise IndexError('pop from empty queue.')
        if self.queue[0][0] == self.maxInQueue[0][0]:
            self.maxInQueue.popleft()
        self.queue.popleft()

    def max(self):
        if len(self.queue) == 0:
            raise IndexError('max from empty queue.')
        return self.maxInQueue[0][1]



if __name__ == '__main__':
    queue = QueueWithMax()
    # {2}
    queue.push_back(2);
    print(queue.queue)

    # {2, 3}
    queue.push_back(3);
    print(queue.queue)

    # {2, 3, 4}
    queue.push_back(4);
    print(queue.queue)

    # {2, 3, 4, 2}
    queue.push_back(2);
    print(queue.queue)

    # {3, 4, 2}
    queue.pop_front();
    print(queue.queue)

    # {4, 2}
    queue.pop_front();
    print(queue.queue)

    # {2}
    queue.pop_front();
    print(queue.queue)

    # {2, 6}
    queue.push_back(6);
    print(queue.queue)

    # {2, 6, 2}
    queue.push_back(2);
    print(queue.queue)

    # 6
    print('Max In Queue: ', queue.max())
