class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # 1. Create a sorted copy of the array
        sorted_nums = sorted(nums)
        
        # 2. Map each number to its first index in the sorted array
        mapping = {}
        for i, num in enumerate(sorted_nums):
            if num not in mapping:
                mapping[num] = i
                
        # 3. Build the result using the dictionary
        return [mapping[num] for num in nums]