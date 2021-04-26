class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        arr = [0]*26
        ans = 0
        for i in chars:
            arr[ord(i)-97]+=1
        for i in words:
            t = arr.copy()
            flag = True
            for j in i:
                if t[ord(j)-97] == 0:
                    flag = False
                    break
                t[ord(j)-97]-=1
            if flag:
                ans += len(i)
        return ans
