class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #populate with unique i,j,l
        triplets = []

        nums.sort()

        #first loop considering i
        for index, value in enumerate(nums):

            #if i is same as previous value: it has already been evaluated
            if (index>0) & (value == nums[index-1]):
                continue

            left = (index + 1)
            right = (len(nums) - 1)

            while left < right:

                currentSum = value + nums[left] + nums[right]

                if currentSum > 0:

                    right -= 1
                
                elif currentSum < 0:

                    left += 1
                else:
                    triplets.append([value, nums[left], nums[right]])

                    left +=1

                    #keeps looking for more solutions

                    while (left < right) & (nums[left] == nums[left-1]):
                        left+=1
        return triplets



            
        