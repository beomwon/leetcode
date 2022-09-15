class Solution:
    def isHappy(self, n):
        before = [n]
        while True:
            if n == 1: return True
            n = sum([int(v)**2 for v in list(str(n))])
            if n in before:
                return False
            before.append(n)