class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
            # skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare the two characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True