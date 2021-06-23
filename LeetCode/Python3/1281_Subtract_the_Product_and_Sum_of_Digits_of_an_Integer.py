class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        #return eval('*'.join(str(n))) - eval('+'.join(str(n)))
        prod = 1
        summa = 0
        for i in str(n):
            prod *= int(i)
            summa += int(i)
        return prod - summa
