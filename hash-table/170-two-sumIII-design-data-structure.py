'''
Two Sum III - Data structure design
===================================
Design and implement a TwoSum class. It should support the following
operations: add and find.
add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the
value.
For example,
    add(1); add(3); add(5);
    find(4) -> true
    find(7) -> false
'''


class TwoSum(object):
  def __init__(self):
    """
    initialize your data structure here
    """
    self.nums = []

  def add(self, number):
    """
    Add the number to an internal data structure.
    :rtype: nothing
    """
    self.nums.append(number)


  def find(self, value):
    """
    Find if there exists any pair of numbers which sum is equal to the value.
    :type value: int
    :rtype: bool
    """
    c = {}
    for num in self.nums:
      if num in c:
        return True
      c[value - num] = num
    return False


s = TwoSum()
s.add(10)
s.add(13)
s.add(1)
s.add(5)
s.add(24)
s.add(6)

print(s.find(7))

