class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0

        for i in range(len(nums)):
            if nums[r]!=nums[l]:
                l+=1
                nums[l],nums[r] = nums[r],nums[l]
                r += 1
            else:
                r +=1

        return l+1
