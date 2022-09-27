class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        word = ""
        last = len(s)-1
        for i in range(len(s)):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z':
                while(True):
                    if 'a' <= s[last] <= 'z' or 'A' <= s[last] <= 'Z':
                        word += s[last]
                        last -= 1
                        break
                    last -= 1
            else:
                word += s[i]
                
        return word
                