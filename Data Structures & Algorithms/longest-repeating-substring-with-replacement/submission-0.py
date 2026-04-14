class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #increment s[r] in the hashmap
            maxf = max(maxf, count[s[r]]) # setting maximum frequency 
                                            # to the character that appears most in the window
            
            while (r - l + 1) - maxf > k: # while the numbers to replace is greater than k
                count[s[l]] -= 1 # updating hashmap as our window shifts
                l += 1 # shifting left pointer
            
            # now our window has reached the maximum replacement length
            res = max(res, r - l + 1) # reassign res if our window is bigger
        
        return res

