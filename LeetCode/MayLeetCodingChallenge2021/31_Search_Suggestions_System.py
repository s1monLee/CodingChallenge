class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        word = ""
        products = sorted(products)
        for i in searchWord:
            word += i
            t = []
            for s in products:
                if s.startswith(word):
                    t.append(s)
                if len(t) == 3:
                    break
            ans.append(t)
        return ans
            
