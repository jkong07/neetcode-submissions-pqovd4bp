class Solution:
    def isAnagram(self, s: str, t: str):
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = []
        dup = []

        for i in range(len(strs)):
            l = []
            if strs[i] not in dup:
                l.append(strs[i])
                dup.append(strs[i])
                for j in range(i + 1, len(strs)):
                        if self.isAnagram(strs[i], strs[j]):
                            l.append(strs[j])
                            dup.append(strs[j])
                arr.append(l)
        return arr
            




        