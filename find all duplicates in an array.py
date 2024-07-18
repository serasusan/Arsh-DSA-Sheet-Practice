class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in nums:
            i = abs(i)
            if nums[i-1]<0:
                ans.append(i)
            else:
                nums[i-1] = -nums[i-1]

        return ans
            
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
