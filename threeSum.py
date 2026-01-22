'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
'''


from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums.sort()
     
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threesum = nums[i] + nums[j] + nums[k]
                if threesum > 0:
                    k -= 1
                elif threesum < 0:
                    j += 1
                else:
                    triplets.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1

        return list(triplets)