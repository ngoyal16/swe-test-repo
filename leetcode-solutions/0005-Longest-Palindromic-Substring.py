"""
LeetCode Problem #5: Longest Palindromic Substring

This solution implements a method to find the longest palindromic substring within a given string. The approach involves expanding around the center for both even and odd length palindromes, checking each substring for palindrome properties, and updating the maximum length palindrome found.

Time Complexity: O(n^2), where n is the length of the string. This is because for each character, we potentially expand in both directions to check for palindromes.
Space Complexity: O(1), as no additional space is required apart from variables used for tracking purposes.

Assumptions:
- The input string is non-null and can be of any length.
- The solution is focused on finding the longest palindromic substring, not all palindromic substrings.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not isinstance(s, str) or len(s) == 0:
            return ""
        
        maxLen = 1
        start = 0
        for i in range(1, len(s)):
            # Check for even length palindrome
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

            # Check for odd length palindrome
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(s) and s[low] == s[high]:
                if high - low + 1 > maxLen:
                    start = low
                    maxLen = high - low + 1
                low -= 1
                high += 1

        return s[start:start + maxLen]