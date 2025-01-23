class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = set(nums)
        for i in nums:  
          while nums.count(i) > 2:
            nums.remove(i)
        print(nums)