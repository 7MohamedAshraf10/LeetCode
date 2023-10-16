class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the idea is to know the number of non-zeros elements
        # then I would know the number of zero elements (length of list - number of non-zero)
        # After that add (length of list - number of non-zero) zero elements to the list 
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[count] = nums[i]
                count +=1
        
        while count < len(nums):
            nums[count] = 0
            count+=1
        
