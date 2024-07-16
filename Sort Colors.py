class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zeros, ones, twos, n = 0,0,0,len(nums)

        # for num in nums:
        #     if num == 0:
        #         zeros += 1
        #     elif num == 1:
        #         ones += 1
        #     else:
        #         twos += 1
        # for i in range(0,zeros):
        #     nums[i] = 0
        # for i in range(zeros,zeros+ones):
        #     nums[i] = 1
        # for i in range(zeros + ones,n):
        #     nums[i] = 2


        # Bubble Sort

        # n = len(nums)
        # for i in range(n):
        #     swapped = False
        #     for j in range(n-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j],nums[j+1]=nums[j+1],nums[j]
        #             swapped = True
        #     if swapped == False:
        #         break


        # Dutch National Flag Algorithm

        n = len(nums)
        low, mid, high = 0, 0, n-1

        while(mid<=high):
            if nums[mid]==2:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -=1
            elif nums[mid] == 0:
                nums[low],nums[mid] = nums[mid], nums[low]
                mid +=1
                low +=1
            else:
                mid +=1
                
