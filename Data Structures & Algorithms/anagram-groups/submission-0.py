class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_anagram=defaultdict(list)
        for s in strs:
            s_ascii=[0]*26
            for char in s:
                s_ascii[ord(char)-ord('a')]+=1
            result_anagram[tuple(s_ascii)].append(s)
        return result_anagram.values()
        