"""
Given a non-empty string containing an out-of-order English representation of digits 0-9, output the digits in ascending order.

Note:

    Input contains only lowercase English letters.
    Input is guaranteed to be valid and can be transformed to its original digits. That means invalid inputs such as "abc" or "zerone" are not permitted.
    Input length is less than 50,000.
"""

class Solution:
    def originalDigits(self, s: str) -> str:
        ans = {}
        cnt = Counter(s)
        ans[0] = cnt['z']
        ans[2] = cnt['w']
        ans[4] = cnt['u']
        ans[6] = cnt['x']
        ans[8] = cnt['g']
        
        ans[3] = cnt['h'] - ans[8]
        ans[5] = cnt['f'] - ans[4]
        ans[7] = cnt['s'] - ans[6]
        
        ans[1] = cnt['o'] - ans[0] - ans[2] - ans[4]
        ans[9] = cnt['i'] - ans[5] - ans[6] - ans[8]
        
        out = ""
        for i in range(10):
            out += str(i) * ans[i]
        return out
