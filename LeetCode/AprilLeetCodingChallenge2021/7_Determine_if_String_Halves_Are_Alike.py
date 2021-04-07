class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        #vowel = {'a','e','i','o','u','A','E','I','O','U'}
        vowel = set('aeiouAEIOU')
        counter = 0
        for i in range(len(s)//2):
            if s[i] in vowel:
                counter += 1
            if s[-i-1] in vowel:
                counter -= 1
        return counter == 0
