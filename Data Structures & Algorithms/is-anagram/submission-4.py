class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count_map, t_count_map = {}, {}
        for i in range(len(s)):
            s_count_map[s[i]] = s_count_map.get(s[i], 0) + 1
            t_count_map[t[i]] = t_count_map.get(t[i], 0) + 1
        return s_count_map == t_count_map 

        