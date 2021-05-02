class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alf = [0]*26
        for i in sentence:
            alf[ord(i)-97]+=1
        for i in alf:
            if i == 0:
                return False
        return True
