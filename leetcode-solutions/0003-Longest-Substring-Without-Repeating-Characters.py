"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Approach: Use a sliding window technique to maintain a substring without repeating characters. Expand the window by moving the right pointer, and shrink it by moving the left pointer when a repeat character is found.
Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(min(m, n)), where m is the size of the charset/alphabet and n is the size of the string.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        left = 0
        right = 0
        ans = 0
        while right < len(s):
            if s[right] in charMap:
                left = max(left, charMap[s[right]] + 1)
            charMap[s[right]] = right
            ans = max(ans, right - left + 1)
            right += 1
        return ans

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("") == 0
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    print("All tests passed.")