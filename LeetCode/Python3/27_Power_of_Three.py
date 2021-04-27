class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0 # 3**19
        """
        if n <= 0: return False
        while n > 1:
            if n%3: return False
            n //= 3
        return True
        """
        """
        if n <= 0: return False
        res = round(log(n, 3))
        return 3**res == n
        """
