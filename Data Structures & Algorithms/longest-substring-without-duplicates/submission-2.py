class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        index_mapping={}
        l,max_len=0,0
        for r in range(len(s)):
            if s[r] in index_mapping:
                l=max(index_mapping[s[r]]+1,l)
            index_mapping[s[r]]=r
            max_len=max(max_len,r-l+1)
        return max_len

        