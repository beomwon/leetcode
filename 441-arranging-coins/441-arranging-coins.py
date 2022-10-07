class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = 1
        while n > 0:
            r += 1
            n -= r
        return r - 1