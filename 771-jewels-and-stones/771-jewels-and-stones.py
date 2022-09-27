class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        before = len(stones)
        for v in list(jewels):
            stones = stones.replace(v, "")
        return before - len(stones)