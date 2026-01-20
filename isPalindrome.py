'''
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        print(s)

        start = 0
        end = len(s) - 1
        while start < end:
            if s[start].lower() != s[end].lower() :
                return False
            start += 1
            end -= 1
        return True