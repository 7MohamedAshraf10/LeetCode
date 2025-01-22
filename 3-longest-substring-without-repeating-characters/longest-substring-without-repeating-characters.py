class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subStr = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):

            if char in subStr and subStr[char] >= start:
                start = subStr[char] + 1
            
            subStr[char] = end
        
            max_length = max(max_length, end - start + 1)
        
        return max_length