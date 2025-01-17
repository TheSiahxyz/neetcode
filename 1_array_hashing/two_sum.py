"""
Question

Two Integer Sum

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: nums = [3,4,5,6], target = 7

Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]

Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]

Constraints:

    2 <= nums.length <= 1000
    -10,000,000 <= nums[i] <= 10,000,000
    -10,000,000 <= target <= 10,000,000
"""

from typing import Dict, List


class Solution:
    def hashmap(self, nums: List[int], target: int) -> List[int]:
        hm: Dict = {}
        for i, n in enumerate(nums):
            if target - n in hm:
                return [hm[target - n], i]
            hm[n] = i
        return [-1, -1]


case1 = [3, 4, 5, 6]
target1 = 7
case2 = [4, 5, 6]
target2 = 10
case3 = [5, 5]
target3 = 10

solution = Solution()
print(f" hashmap case1: {solution.hashmap(case1, target1)}")
print(f" hashmap case2: {solution.hashmap(case2, target2)}")
print(f" hashmap case3: {solution.hashmap(case3, target3)}")


"""
Solution

url: https://neetcode.io/problems/two-integer-sum
video: https://youtu.be/KLlXCFG5TnA

1. hashmap
time: O(n)
space: O(n)
code:
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```
"""
