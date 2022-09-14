class Solution:
    def reverseBits(self, n: int) -> int:
        return int('0b' + ('%32s' % format(n, 'b')).replace(' ','0')[::-1], 2)