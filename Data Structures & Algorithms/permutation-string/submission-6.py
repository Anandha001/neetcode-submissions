class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        s1count , s2count = [0]*26,[0]*26
        l, matches =0, 0
        for i in range(len(s1)):
            s1count[ord(s1[i])-ord('a')]+=1
            s2count[ord(s2[i])-ord('a')]+=1

        for i in range(26):
            if s1count[i] == s2count[i]:
                matches+=1

        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            current_index = ord(s2[r])-ord('a')
            s2count[current_index]+=1
            if s1count[current_index] == s2count[current_index]:
                matches +=1
            elif s1count[current_index] + 1 ==s2count[current_index]:
                matches-=1
            
            current_index = ord(s2[l])-ord('a')
            s2count[current_index]-=1
            if s1count[current_index] == s2count[current_index]:
                matches+=1
            elif s1count[current_index]-1 == s2count[current_index]:
                matches-=1
            
            l+=1
        return matches == 26
        