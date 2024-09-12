"""
Question

Anagram Groups

Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]

Constraints:

    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.
"""

from collections import defaultdict
from typing import Dict, List


class Solution:
    def dictionary(self, strs: List[str]) -> List[List[str]]:
        res: Dict = defaultdict(list)
        for s in strs:
            count: List[int] = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


case1 = ["act", "pots", "tops", "cat", "stop", "hat"]
case2 = ["x"]
case3 = [""]

solution = Solution()
print(f" dictionary case1: {solution.dictionary(case1)}")
print(f" dictionary case2: {solution.dictionary(case2)}")
print(f" dictionary case3: {solution.dictionary(case3)}")


"""
Solution

url: https://neetcode.io/problems/anagram-groups
video: https://youtu.be/vzdNOK2oB2E

1. dictionary
time: O(m*n*26) = O(m*n)
space: O()
code:
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()
```
"""
