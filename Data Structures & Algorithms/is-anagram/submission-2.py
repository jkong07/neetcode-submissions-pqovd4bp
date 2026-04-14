class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        MyMap = {}
        MyMap1 = {}

        for n in s:
            MyMap[n] = MyMap.get(n, 0) + 1
        
        for n in t:
            MyMap1[n] = MyMap1.get(n, 0) + 1
        
        return MyMap == MyMap1

        