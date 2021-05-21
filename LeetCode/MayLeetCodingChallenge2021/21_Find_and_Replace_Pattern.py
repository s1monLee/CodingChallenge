class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        def str_to_dig(p:str) -> str:
            i = 0
            while i < len(p):
                ch = p[i]
                if(ord(ch)>96):
                    p=p.replace(ch,str(i))
                i+=1
            return p
        pattern = str_to_dig(pattern)
        for i in words:
            word = str_to_dig(i)
            if word == pattern:
                ans.append(i)
        return ans
