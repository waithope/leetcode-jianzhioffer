

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## Original Solution
        # l1_num = 0
        # l2_num = 0
        # cnt1 = 0
        # cnt2 = 0
        # sum_val = 0
        # current_node1 = l1
        # current_node2 = l2
        # while current_node1 is not None:
        #     l1_num += current_node1.val*(10**cnt1)
        #     cnt1 += 1
        #     current_node1 = current_node1.next
        # while current_node2 is not None:
        #     l2_num += current_node2.val*(10**cnt2)
        #     cnt2 += 1
        #     current_node2 = current_node2.next
        # sum_val = str(l1_num + l2_num)
        # l_head = ListNode(int(sum_val[len(sum_val) - 1]))
        # current_head = l_head
        # for i in range(len(sum_val) - 2, -1, -1):
        #     temp = ListNode(int(sum_val[i]))
        #     current_head.next = temp
        #     current_head = temp
        # return l_head

        ## Improved Version
        l = ListNode(0)
        aux = l
        carry = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            sum_ = l1.val + l2.val + carry
            carry = sum_ // 10
            remainder = sum_ % 10
            aux.next = ListNode(remainder)
            aux = aux.next
            l1 = l1.next
            l2 = l2.next
        if carry is not 0:
            aux.next = ListNode(carry)
        return l.next