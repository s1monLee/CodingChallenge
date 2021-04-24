"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""
#O(N)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        num = 0
        for i in range(n):
             num ^= start + 2*i
        return num
      
"""
#O(1)
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n == 1: return start

        last = start + 2 * (n - 1)
        if start % 4 <= 1:
            if n % 4 == 0:
                return 0
            elif n % 4 == 1:
                return last
            elif n % 4 == 2:
                return 2
            else:
                return 2 ^ last
        else:
            if (n - 1) % 4 == 0:
                return start
            elif (n - 1) % 4 == 1:
                return start ^ last
            elif (n - 1) % 4 == 2:
                return start ^ 2
            else:
                return start ^ 2 ^ last
"""
