class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = t_point = 0
        while (s_point < len(s)) and (t_point < len(t)):
            if s[s_point] == t[t_point]:
                s_point += 1
            t_point+=1
        return s_point == len(s)