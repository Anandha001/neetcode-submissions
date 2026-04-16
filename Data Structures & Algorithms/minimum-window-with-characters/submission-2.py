class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        scount,tcount={},{}
        for i in range(len(t)):
            tcount[t[i]]=1+tcount.get(t[i],0)

        have,need=0,len(tcount)
        min_ind,min_res=[-1,-1],float("infinity")

        l=0
        for r in range(len(s)):
            char=s[r]
            scount[char]=1+scount.get(char,0)

            if char in tcount and scount[char]==tcount[char]:
                have+=1
            
            while have==need:
                slen=r-l+1
                if slen< min_res:
                    min_res=slen
                    min_ind=[l,r]

                scount[s[l]]-=1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                
                l+=1
        
        l,r =min_ind

        return s[l:r+1] if min_ind!=float("infinity") else ""
            


        