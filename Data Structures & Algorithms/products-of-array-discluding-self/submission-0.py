class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Create an output list filled with 1s, same length as nums
        # We'll build the final answer into this list
        result = [1] * (len(nums))

        # --- PASS 1: Prefix products (left side) ---
        # prefix tracks the running product of everything to the LEFT of index i
        prefix = 1
        for i in range(len(nums)):
            # Store the product of all elements before index i
            result[i] = prefix
            # Then multiply prefix by current element to include it for the next index
            prefix *= nums[i]

        # After this loop, result[i] = product of all numbers to the LEFT of i

        # --- PASS 2: Postfix products (right side) ---
        # postfix tracks the running product of everything to the RIGHT of index i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # loop backwards
            # Multiply what's already in result[i] (left product) by the right product
            result[i] *= postfix
            # Then multiply postfix by current element to include it for the next index
            postfix *= nums[i]

        # After this loop, result[i] = (left product) * (right product) = product of everything except itself

        return result