class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        left = 0
        result = 0
        for right in range(len(s)):
            #if character is already inside set = duplicate
            while s[right] in charSet:
                #remove left most character
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            result = max(result, right - left + 1)
        return result
            
