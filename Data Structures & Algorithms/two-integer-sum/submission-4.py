class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #stores numbers
        visitedNums = {}

        for currentIndex, currentNum in enumerate(nums):
            neededNum = target - currentNum

            if neededNum in visitedNums:
                return[visitedNums[neededNum], currentIndex]
            
            visitedNums[currentNum] = currentIndex