class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        str_map = {}
        for r in range(len(s)):
            if s[r] in str_map:
                l = max(str_map[s[r]] + 1, l)
            max_len =max(max_len, r-l+1)
            str_map[s[r]] = r

        return max_len        