'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            count = [0] * 26    #create array of 26 0's (each maps to one alphabet)
            
            #store count of each character at index
            for char in string:
                count[ord(char) - ord('a')] += 1    #ord() converts char into int representation         
            #convert key to a tuple so it is immutable
            key = tuple(count)  #keys should not change ever!
            groups[key].append(string)
            
        return list(groups.values())