class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res_length = 0
        char_map = {}

        for right in range(len(s)):
            char = s[right]
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right

            res_length = max(res_length, right - left + 1)
        return res_length