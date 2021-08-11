"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximal = start = 0
        letters = {}
        for i, c in enumerate(s):
            if c in letters and letters[c] >= start:
                start = letters[c] + 1
            else:
                maximal = max(maximal, i - start + 1)
            letters[c] = i
        return maximal
