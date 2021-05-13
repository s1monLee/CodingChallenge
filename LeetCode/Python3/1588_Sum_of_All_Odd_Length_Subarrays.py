"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0; freq = 0; n = len(arr)
        for i in range(n):
            freq = freq-(i+1)//2+(n-i+1)//2
            res += freq*arr[i]
        return res
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr),2):
                ans += sum(arr[i:j+1])
        return ans
                
