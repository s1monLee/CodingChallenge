class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        item = 0
        rule = { "type":0,
                "color":1,
                 "name":2
               }
        for i in items:
            if ruleValue == i[rule[ruleKey]]:
                item+=1
        return item
