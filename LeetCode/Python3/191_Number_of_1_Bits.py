class Solution: 
    def hammingWeight(self, n: int) -> int: 
        return sum(list(map(int,bin(n)[2:])))
