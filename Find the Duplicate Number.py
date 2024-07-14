class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index]<0:
                return index
            nums[index] = -nums[index]

        return -1


# Day 1
# Learned about Floyd's tortoise and hare algorithm
# https://www.youtube.com/watch?v=PvrxZaH_eZ4
