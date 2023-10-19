class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_zeros = 0
        left = 0
        zeros = 0
        for right, n in enumerate(nums):
            if n == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_zeros = max(max_zeros, right - left + 1)
        return max_zeros