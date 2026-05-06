class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in sum:
                return [sum[difference], i]
            sum[n] = i