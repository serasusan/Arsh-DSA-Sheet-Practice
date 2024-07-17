class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1 # l->buy, r->sell
        maxProfit = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r
            r+=1
        return maxProfit

        
        
        
        
        # profit = 0
        # for i in range(0,len(prices)):
        #     for j in range(i+1,len(prices)):
        #         temp_profit = prices[j]-prices[i]
        #         if(temp_profit > profit):
        #             profit = temp_profit
        # return profit

# # this is incorrect code
# class Solution:
#     def maxProfit(self,nums:List[int]) -> int:
#         min_val = min(nums)
#         max_val = 0
#         min_val_index = nums.index(min_val)

#         if min_val_index != len(nums)-1:
#             max_val = max(nums[min_val_index+1:len(nums)])
#         else:
#             min_val = 0
        
#         return max_val - min_val
        
        
