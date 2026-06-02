class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s):
            return ""

        scount, tcount = {}, {}
        for i in range(len(t)):
            tcount[t[i]] = tcount.get(t[i],0) + 1
        
        have, need = 0, len(tcount)
        min_res, min_ind = float('infinity'), [-1,-1]

        l=0
        for r in range(len(s)):
            char = s[r]
            scount[char]= scount.get(char,0)+1

            if char in tcount and scount[char] == tcount[char]:
                have+=1
            
            while have == need:
                temp_min_res = r-l+1

                if temp_min_res < min_res:
                    min_res= temp_min_res
                    min_ind = [l,r]

                scount[s[l]]-=1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1

                l+=1
            
        l,r = min_ind[0], min_ind[1]

        return s[l:r+1]if min_res != float('infinity') else ""

        