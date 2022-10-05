class Solution:
    def calPoints(self, op):
        res = []
        
        for v in op:
            if v == 'C': res.pop()
            elif v == 'D': res.append(res[-1]*2)
            elif v == '+': res.append(sum(res[-2:]))
            else: res.append(int(v))
                
        return sum(res)