'''
You are given an integer array heights where heights[i] represents the height of the i'th bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.
'''

from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer approach  
        left, right = 0, len(heights) - 1
        area = float('-inf')

        while left < right:
            height = min(heights[left], heights[right])
            area = max(area, height * (right - left))

            # here, we check if left side is less, only then we move the left pointer forward
            if heights[left] < heights[right]:
                left += 1
            else: # otherwise, we do the opposite i.e. move right pointer backward
                right -= 1
        # this uses O(N) time and O(1) space: only area is updated
        return area