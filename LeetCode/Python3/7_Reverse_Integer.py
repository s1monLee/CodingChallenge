class Solution:
    def reverse(self, x: int) -> int:
        """
        sign = [1,-1][x<0]
        ans = sign * int(str(abs(x))[::-1])
        return ans if -(2**31) < ans < 2**31 else 0
        """
        return [1,-1][x<0]*int(str(abs(x))[::-1]) if -(2**31)<[1,-1][x<0]*int(str(abs(x))[::-1])<2**31 else 0
