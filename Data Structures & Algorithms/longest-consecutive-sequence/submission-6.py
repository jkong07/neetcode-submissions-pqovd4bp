class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        med = set()
        unique = []

        vals = []

        
        for n in nums:
            med.add(n)
        for n in med:
            unique.append(n)
        
        unique.sort()
        
        count = 1
        for i in range(len(unique)-1):
            if unique[i] == (unique[i+1] - 1):
                count += 1
            else:
                vals.append(count)
                count = 1

        vals.append(count)

        return max(vals)


            