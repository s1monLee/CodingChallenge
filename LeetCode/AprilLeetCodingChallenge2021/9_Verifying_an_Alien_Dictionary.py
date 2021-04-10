class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        al = {ch : i for i, ch in enumerate(order)}
        words = [[al[c] for c in w]for w in words]            
        return all(w1<=w2 for w1, w2 in zip(words,words[1:]))
