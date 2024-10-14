"""
Question

Medium

Design an algorithm to encode a list of strings to a single string.
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]

Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]

Constraints:

    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains only UTF-8 characters.
"""

from typing import Dict, List


class Solution:
    """
    A class to solve string encode and decode from input list.
    String encode and decode from the input strs: List[str] using a encode approach.
    """

    def encode(self, strs: List[str]) -> str:
        """
        string encode from the input strs: List[str] using a encode approach.

        Args:
            strs: List[str]: a list of strings

        Returns:
            str: a single string
        """
        res: str = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        """
        string decode from the input str: str using a encode approach.

        Args:
            s: str: a string

        Returns:
            res: List[str] a list of strings
        """
        res: List = []
        i: int = 0

        while i < len(s):
            j: int = i
            while s[j] != "#":
                j += 1
            length: int = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

    def print(self, examples: Dict) -> None:
        """
        funciton to print the result.

        Args:
            example: Dict, a dictionary of examples
        """
        for name, example in examples.items():
            res_encode = self.encode(example)
            print(f"{name}: {res_encode}")
            res_decode = self.decode(res_encode)
            print(f"{name}: {res_decode}")

    def main(self):
        """
        main function to call print function to test examples
        """
        examples = {
            "ex1": ["neet", "code", "love", "you"],
            "ex2": ["we", "say", ":", "yes"],
            "ex3": ["I", "love", "Yejin"],
        }

        # Passing the dictionary to the print method
        self.print(examples)


solution = Solution()
solution.main()


"""
Solution

url: https://neetcode.io/problems/string-encode-and-decode
video: https://www.youtube.com/watch?v=B1k_sxOSgv8&embeds_referring_euri=https%3A%2F%2Fneetcode.io%2F&source_ve_path=Mjg2NjY

1. encode
time: O(n)
space: O(n)
code:
```python
class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res
```
"""
