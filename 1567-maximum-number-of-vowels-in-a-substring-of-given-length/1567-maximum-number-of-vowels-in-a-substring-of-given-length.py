class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'AEIOUaeiou'
        max_vaw = 0
        cur_vaw = 0
        # iterate through each char in the string
        for i in range(len(s)):
            # if the current char is cowel then increase the vowel counter by one
            if s[i] in vowels:
                cur_vaw += 1
            
            # if the window moved right and the first element was vowel, then mins one from the current vowels counter
            if (i >= k) and (s[i - k] in vowels):
                cur_vaw -= 1
            
            max_vaw = max(max_vaw, cur_vaw)
            
        return max_vaw
