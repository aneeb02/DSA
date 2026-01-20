'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
'''
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        # making it better
        difference = 0
        seen = {}
        for i,n  in enumerate(nums):
            seen[n] = i
            
        for i,n in enumerate(nums):
            difference = target - n
            if difference in seen and seen[difference] != i:
                return [i, seen[difference]]
        
        return []

        # alternate approach
        # seen = {}

        # for i, n in enumerate(numbers):
        #     print(i,n)
        #     j = target - n
        #     if j in seen:
        #         return [seen[j]+1, i+1]
        #     seen[n] = i
        # return []    


nums = [2,7,11,15, 3,5,77,14,5,2,621,5,1,4,7,8,9,0]
nums_dict = {}

for i,n in enumerate(nums):
    nums_dict[i] = n
        
print(nums_dict)

