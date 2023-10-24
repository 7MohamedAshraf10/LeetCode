class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Initialize variables to keep track of the sum on the left and right sides.
        left = 0
        right = sum(nums)

        # Iterate through the elements of the 'nums' list along with their indices.
        for i, num in enumerate(nums):
            # Decrement 'right' by the current 'num' to simulate moving it from right to left.
            right -= num

            # Check if the sum of elements on the left and right sides is equal.
            if left == right:
                # If they are equal, return the index 'i' as it's the pivot index.
                return i

            # Increment 'left' by the current 'num' to maintain the balance.
            left += num

        # If no pivot index is found after the loop, return -1 to indicate that there is no pivot.
        return -1
