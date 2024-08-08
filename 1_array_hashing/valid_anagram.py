"""
Question

Is Anagram

Easy

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false

Constraints:
    - s and t consist of lowercase English letters.
"""

class Solution:
    def hashmap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


case1S = "apple"
case1T = "plpea"
case2S = "asneaxl"
case2T = "yejindp"
case3S = "iloveyou"
case3T = "youlovei"

solution = Solution()

print(f"hashmap case1: {solution.hashmap(case1S, case1T)}")
print(f"hashmap case2: {solution.hashmap(case2S, case2T)}")
print(f"hashmap case3: {solution.hashmap(case3S, case3T)}")

"""
Solution
url: https://neetcode.io/problems/is-anagram
video: https://youtu.be/9UtInBqnCgA

1. brute force
time: O(n)
space: O(1)

2. hashmap
time: O(s+t)
space: O(s+t)
code:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
"""
