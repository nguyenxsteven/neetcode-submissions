class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        for num in nums:
            frequency[num]= 1 + frequency.get(num, 0)

        countNumberPairs = []
        for num, count in frequency.items():
            countNumberPairs.append([count, num])
        
        countNumberPairs.sort()

        result = []
        while len(result) < k:
            result.append(countNumberPairs.pop()[1])

        return result