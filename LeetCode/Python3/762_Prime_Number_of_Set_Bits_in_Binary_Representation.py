class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        """
        ans = 0
        for i in range(L, R+1):
            if bin(i)[2:].count('1') in [2, 3, 5, 7, 11, 13, 17, 19]:
                ans += 1
        return ans
        """
        return len([i for i in range(L, R+1) if bin(i)[2:].count('1') in [2, 3, 5, 7, 11, 13, 17, 19]])
