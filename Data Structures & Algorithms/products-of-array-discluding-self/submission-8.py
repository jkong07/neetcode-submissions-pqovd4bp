class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        
        zerocount = 0
        product = 1
        zerop = 1

        for n in nums:
            if n != 0:
                product *= n
            if n == 0:
                zerocount += 1
            zerop *= n

        if zerocount > 1:
            return [0] * len(nums)
        
        for n in nums:
            if n != 0:
                res.append(int(zerop/n))
            if n == 0:
                res.append(product)

        return res