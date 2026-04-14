class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        mp1 = {}
        mp2 = {}

        for c in s1:
            mp1[c] = 1 + mp1.get(c, 0)
        
        for i in range(len(s1)):
            mp2[s2[i]] = 1 + mp2.get(s2[i], 0)
        
        if mp1 == mp2:
            return True
        
        l,r = 0, len(s1) - 1

        while r < len(s2) - 1:
            mp2[s2[l]] -= 1
            if mp2[s2[l]] == 0:
                del mp2[s2[l]]
            l += 1
            
            r += 1
            mp2[s2[r]] = 1 + mp2.get(s2[r], 0)

            if mp1 == mp2:
                return True
        
        return False
            

