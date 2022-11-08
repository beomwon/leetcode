class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        
        for v in s:
            s = s.replace(v,'')
            t = t.replace(v,'')
            if len(s) != len(t):
                return False
            
        return True

        