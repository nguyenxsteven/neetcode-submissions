class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
          # Set to store numbers we've seen so far
        seen = set()

        # Check each number
        for num in nums:
            # If we've seen this number before, a duplicate exists
            if num in seen:
                return True
            # Mark this number as seen
            seen.add(num)

        # No duplicates found
        return False

    
