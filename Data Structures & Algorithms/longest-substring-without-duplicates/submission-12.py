class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        dups = {s[0] : 0}
        l,r = 0, 1
        longest = 1

        while r < len(s):
            if s[r] in dups:
                l = max(l, dups[s[r]] + 1)
            longest = max(longest, r - l + 1)
            dups[s[r]] = r
            r += 1
        return longest



                
