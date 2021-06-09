class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        dic = {}
        for i in arr1:
            if dic.get(i) == None:
                dic[i] = 1
            else:
                dic[i]+=1
        ans = []
        for i in arr2:
            ans+=[i]*dic[i]
        ext = []
        for i in set(arr1) - set(arr2):
            ext += [i]*dic[i]
        return ans + sorted(ext)
