# https://leetcode.com/problems/container-with-most-water/description/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        w = n-1
        l = 0
        r = n
        maxArea = float(-inf)
        while r>l:
            area = w*(min(height[l],height[r]))
            maxArea = max(area,maxArea)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
            w = w-1
        return maxArea
