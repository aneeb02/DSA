'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
'''


# starting solution: sort, then check char by char
# def isAnagram(self, s: str, t: str) -> bool:
#     s = sorted(s)
#     t = sorted(t)

#     if len(s) != len(t):
#         return False
#     for i in range(len(s)):
#         if s[i] == t[i]:
#             continue
#         else:
#             return False
#     return True   

from collections import Counter
def isAnagram(self, s: str, t: str) -> bool:
    #convert to dict
    s_counts = Counter(s)
    t_counts = Counter(t)

    #check if both are equal
    return s_counts == t_counts
  
# #alternate
# def isAnagram(self, s: str, t: str) -> bool:
#     if len(s) != len(t):
#       return False
#     count = {}
#     for char in s:
#       count[char] = count.get(char,0) + 1
    
#     for char in t:
#       if char not in count or count[char] == 0:
#         return False
#       count[char] -= 1
      
#     return True





