# Method 1
# By marking the visited node negative. The node corresponding to the index value(i.e. the visited node), will be made negative

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

# Method 2
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # This is similar to a linked list, due to the conditions mentioned
        slow = nums[0]
        fast = nums[0]

        # check if there is loop. If there is loop slow == fast. i.e. they'll meet somewhere
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Now find the entry point
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
