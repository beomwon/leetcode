class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start, last = 0, len(s)
        res = []
        for v in list(s):
            if v == "I":
                res.append(start)
                start += 1
            else:
                res.append(last)
                last -= 1
        if s[-1] == "I": res.append(start)
        else: res.append(last)
        
        return res