class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        pos = [i for i, letter in enumerate(s) if letter == c]
        a = [math.inf]*len(s)
        for i in range(len(s)):
            for j in pos:
                a[i] = min(a[i], abs(i-j))
        return a
