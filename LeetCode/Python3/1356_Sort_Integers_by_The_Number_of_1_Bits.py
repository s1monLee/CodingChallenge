def sortByBits(self, A):
        return sorted(A, key=lambda a: [bin(a).count('1'), a])
"""
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x : (sum((x>>i)&1 for i in range(32)), x))
"""
