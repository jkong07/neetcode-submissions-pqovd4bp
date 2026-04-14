class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        i,j = 0, len(height) - 1
        maxL = height[i]
        maxR = height[j]

        while i < j:
            if maxL < maxR:
                i += 1
                total += max(0, maxL - height[i])
                maxL = max(maxL, height[i])
            else:
                j -= 1
                total += max(0, maxR - height[j])
                maxR = max(maxR, height[j])
        return total


