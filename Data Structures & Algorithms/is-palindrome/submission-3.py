class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ''
        for character in s:
            if character.isalnum(): # checks if char is alpha numeric which is letters and numbers
                newString += character.lower() # turns character to lowercase

        return newString == newString [::-1] # checks if string reads the same backwards and forwards, -1 reverses string
