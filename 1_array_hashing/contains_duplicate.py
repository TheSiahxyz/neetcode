"""
Question

Duplicate Integer

Easy

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""


from typing import List


class Solution:
    # 1. brute force
    def brute_force(self, nums: List[int]) -> bool:
        return False

    # 2. sorting
    def sorting(self, nums: List[int]) -> bool:
        return False

    # 3. hashset
    def hashset(self, nums: List[int]) -> bool:
        hs = set()
        for i in range(len(nums)):
            if nums[i] in hs:
                return True
            hs.add(nums[i])
        return False


case1 = [1, 2, 3, 4, 5]
case2 = [2, 2, 3, 4, 5]
case3 = [3, 4, 1, 6, 3]
solution = Solution()
print(f"hashset case1: {solution.hashset(case1)}")
print(f"hashset case2: {solution.hashset(case2)}")
print(f"hashset case3: {solution.hashset(case3)}")


"""
Solution

url: https://neetcode.io/problems/duplicate-integer
video: https://youtu.be/3OamzN90kPg

1. brute force
time: O(n^2)
space: O(1)

2. sort
time: O(nlogn)
space: O(1)

3. hashset
time: O(n)
space: O(n)
code:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
"""
