class Solution:
    def getRow(self, numRows):
        res = [[1],[1,1]]
        if numRows == 0: return [1]
        if numRows == 1: return [1,1]
        
        for step in range(2, numRows+1):
            temp = []
            for i in range(1, len(res[step-1])):
                temp.append(res[step-1][i-1] + res[step-1][i])
            res.append([1] + temp + [1])
        
        return res[-1]
        