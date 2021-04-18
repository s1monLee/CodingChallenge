class Solution:
    def numberOfSteps(self, num: int) -> int:
        numbit = bin(num)
        return len(numbit[2:]) - 1 + numbit.count('1')
