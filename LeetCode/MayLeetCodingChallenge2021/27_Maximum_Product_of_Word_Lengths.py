class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = []
        prod = 0
        for word in words:
            sets.append(set(word))
        for i, x in enumerate(sets):
            for j, y in enumerate(sets):
                if x.isdisjoint(y):
                    prod = max(prod, len(words[i])*len(words[j]))
        return prod
