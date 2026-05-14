class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)  # Store array length
        res = [1] * n  # Initialize result array with 1s

        prefix = 1  # Running product of elements to the left
        for i in range(n):  # Left-to-right pass
            res[i] = prefix  # Store product of all elements before i
            prefix *= nums[i]  # Update prefix with current element

        suffix = 1  # Running product of elements to the right
        for i in range(n - 1, -1, -1):  # Right-to-left pass
            res[i] *= suffix  # Multiply by product of all elements after i
            suffix *= nums[i]  # Update suffix with current element

        return res  # Return final answer













        