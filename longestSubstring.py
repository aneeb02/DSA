'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # empty string, no substring
        if len(s) == 0:
            return 0

        left, right = 0, 0
        count = 0
        seen = set()

        # slide a window for substring
        while right < len(s):
            # increase window size if unique character is seen and add it to set
            if s[right] not in seen:
                seen.add(s[right])
                count = max(count, 1 + right-left)
                right += 1
            # move window forward
            else:
                seen.discard(s[left])
                left += 1

        return count
    