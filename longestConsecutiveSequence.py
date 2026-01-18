'''
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. The elements do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
'''

from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # seen = set()
        # count = 1
        # counts = [1] * len(nums)
        # print (nums)
        # if len(nums) == 0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i+1] - nums[i] == 1 and nums[i+1] not in seen:
        #         counts[i] += 1
        #         seen.add(nums[i])
        # print(seen)
        # maxi = float("-inf")
        # for count in counts:
        #     if maxi < count:
        #         maxi = count
        # return maxi

        # create set for O(1) lookups
        seq = set(nums)
        
        # edge cases
        # check empty array -> return 0
        if len(nums) == 0:
            return 0
        # single element array
        if len(nums) == 1:
            return 1

        longestSequence = 0
        for num in nums:
            # mark start of sequence
            if (num-1) not in seq:
                length = 1
                # if sequence started, keep checking for next elements
                while (num + length) in seq:
                    length +=1
                longestSequence = max(length, longestSequence)
                
        return longestSequence      
