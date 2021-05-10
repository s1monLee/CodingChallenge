class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        j = 0
        for i in range(1, n+1):
            ans.append("Push")
            if i != target[j]:
                ans.append("Pop")
                continue
            j += 1
            if j >= len(target):
                break
        return ans
