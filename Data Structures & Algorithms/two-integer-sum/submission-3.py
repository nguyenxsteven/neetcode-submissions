class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            # Calculate what number we'd need to pair with n to reach the target
            difference = target - n
            # Check if we've already seen that needed number earlier in the list
            if difference in seen:
                  # Found the pair! Return the earlier number's index and current index
                return[seen[difference], i]
                # Haven't found a pair yet — save this number and its index for future checks
            seen[n] = i
