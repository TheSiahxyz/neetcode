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

Example 3:

Input: s = "asneaxl", t = "jinyedp"

Output: false

Constraints:
    - s and t consist of lowercase English letters.
"""

from typing import Dict


class Solution:
    def hashmap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs: Dict = {}
        ct: Dict = {}

        for i, n in enumerate(s):
            cs[n] = 1 + cs.get(n, 0)
            ct[t[i]] = 1 + ct.get(t[i], 0)
        return cs == ct


caseS1 = "racecar"
caseT1 = "carrace"
caseS2 = "jar"
caseT2 = "jam"
caseS3 = "asneaxl"
caseT3 = "jinyedp"

solution = Solution()

print(f"hashmap case1: {solution.hashmap(caseS1, caseT1)}")
print(f"hashmap case2: {solution.hashmap(caseS2, caseT2)}")
print(f"hashmap case3: {solution.hashmap(caseS3, caseT3)}")

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
```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```
"""
