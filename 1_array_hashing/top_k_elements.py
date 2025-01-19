"""
Question

Top K Elements in List

Medium

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.
"""

from typing import Dict, List, Tuple


class Solution:
    """
    A class to solve top_k_elements from hash
    """

    def hashmap(self, nums: List[int], k: int) -> List[int]:
        """
        Frequent elements from the input nums: List[int] and k: int using a hashmap approach.

        Args:
            nums: List[int]: integer list
            k: int: frequency

        Returns:
            List[int]: elements list
        """
        count: Dict = {}
        freq: List = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for i, c in count.items():
            freq[c].append(i)

        res: List = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return []

    def print(self, examples: Dict[str, Tuple[List[int], int]]) -> None:
        """
        funciton to print the result.

        Args:
            example: Dict, a dictionary of examples
        """
        for name, (param1, param2) in examples.items():
            result = self.hashmap(param1, param2)
            print(f"{name}: {result}")

    def main(self):
        """
        main function to call print function to test examples
        """
        cases = {"case1": ([1, 2, 2, 3, 3, 3], 2), "case2": ([7, 7], 2)}
        self.print(cases)


solution = Solution()
solution.main()


"""
Solution

url: https://neetcode.io/problems/top-k-elements-in-list
video: https://youtu.be/YPTqKIgVk-k

1. Bucket sort
time: O(n)
space: O(n)
code:
```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```

2. Heap sort (max heap)
time: O(k*logn)
space: O(k*logn)

3. Sorting
time: O(n*logn)
space: O(n*logn)
"""
