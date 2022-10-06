class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        d1, d2 = len(num1), len(num2)
        n1, n2 = 0, 0
        
        for i in range(d1):
            n1 += (ord(num1[i])-48)*10**(d1-i-1)
            
        for i in range(d2):
            n2 += (ord(num2[i])-48)*10**(d2-i-1)
        
        res = n1+n2
        return str(res)