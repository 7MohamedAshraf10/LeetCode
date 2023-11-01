class Solution:
    def removeStars(self, s: str) -> str:
        while '*' in s:
            ind = s.find('*')
            if ind > 0:
                s = s[:ind-1] + s[ind+1:]
        return s
    