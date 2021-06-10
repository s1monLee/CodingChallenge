class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        i = j = 0
        while j < k and i < len(s):
            if(s[i] == ' '):
                j+=1
            i+=1
        return s if i == len(s) else s[:i-1]
        """
        return " ".join(s.split()[:k])
