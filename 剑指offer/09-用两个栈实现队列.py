# -*- coding:utf-8 -*-
'''
    用两个栈实现一个队列
=========================
用两个栈实现一个队列。
队列的声明如下：请实现它的两个函数appendTail和deleteHead，分别完成在队列尾部
插入节点和在队列头部删除节点的功能。
'''

class Queue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def appendTail(self, val):
        self.stack1.append(val)
    def deleteHead(self):
        if self.stack1 == self.stack2 == []:
            return
        elif self.stack2 == []:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()


if __name__ == '__main__':
    queue = Queue()
    queue.appendTail(-1)
    queue.appendTail(0)
    queue.appendTail(3)
    queue.appendTail(-9)
    queue.appendTail(10)
    print(queue.deleteHead())
    print(queue.deleteHead())
