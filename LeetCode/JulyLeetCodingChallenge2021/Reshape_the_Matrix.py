class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        arr = sum(mat, [])
        if r*c != len(arr):
            return mat
        tup = zip(*([iter(arr)]*c))
        return map(list, tup)
        
