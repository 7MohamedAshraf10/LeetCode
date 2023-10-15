class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod , right_prod = 1 , 1
        n = len(nums)
        result = [0]*n
        for i in range(n):
            result[i] = left_prod
            left_prod *= nums[i]   
            
        for i in range( n-1 , -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]
            
        return result