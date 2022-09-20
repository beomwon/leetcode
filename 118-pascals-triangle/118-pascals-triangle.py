class Solution:
    def generate(self, numRows):
        res = [[1],[1,1]]
        if numRows <= 2: return res[:numRows]
        
        for step in range(2, numRows):
            temp = []
            for i in range(1, len(res[step-1])):
                temp.append(res[step-1][i-1] + res[step-1][i])
            res.append([1] + temp + [1])
        
        return res
        