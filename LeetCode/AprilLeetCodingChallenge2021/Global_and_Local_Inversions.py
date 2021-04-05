class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        m = 0
        for i in range(len(A)-2):
            m = max(A[i],m)
            if m > A[i+2]:
                return False
        return True
