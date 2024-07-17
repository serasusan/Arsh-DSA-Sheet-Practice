class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        while(r<len(prices)):
            if prices[r]>prices[l]:
                # price increase is continuous eg. [1,2,3,4,2] here between 1 and 4
                if prices[r]>prices[r-1]:
                    profit =prices[r]-prices[r-1] 
                    maxP += profit
                    r +=1
                else:
                    l=r
                    r+=1
                    if r<len(prices):
                        if prices[r]>prices[r-1]:
                            profit =prices[r]-prices[l] 
                            maxP += profit
                            r +=1
            else:
                l = r
                r += 1

        return maxP
