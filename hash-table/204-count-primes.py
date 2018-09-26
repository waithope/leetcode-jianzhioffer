'''
           Count Primes
===================================
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Method: Sieve of Eratosthenes
'''

def countPrimes(n):
  """
  :type n: int
  :rtype: int
  """
  if n < 3:
    return 0
  primes = [True] * n
  primes[0] = primes[1] = False
  for i in range(2, int(n**0.5)+1):
    if primes[i]:
      primes[i**2:n:i] = [False]*len(primes[i**2:n:i])
  return sum(primes)

import unittest

class Test_Count_Primes(unittest.TestCase):
  def test_count_primes(self):
    self.assertEqual(countPrimes(10), 4)
    self.assertEqual(countPrimes(121), 30)


if __name__ == '__main__':
  unittest.main()