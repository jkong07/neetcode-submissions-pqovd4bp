class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            for j, n in enumerate(nums):
                if j != i:
                    product = product * n
            res.append(product)
        return res
