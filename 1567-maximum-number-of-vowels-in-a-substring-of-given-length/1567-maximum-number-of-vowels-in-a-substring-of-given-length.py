class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('AEIOUaeiou')
        max_vaw = 0
        cur_vaw = 0
        
        for i in range(len(s)):
            if s[i] in vowels:
                cur_vaw += 1
            
            if (i >= k) and (s[i - k] in vowels):
                cur_vaw -= 1
            
            max_vaw = max(max_vaw, cur_vaw)
            
        return max_vaw
