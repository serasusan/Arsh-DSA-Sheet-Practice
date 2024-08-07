# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum_left = sum(cardPoints[0:k])
        sum_right = 0

        n = len(cardPoints)
        
        res = sum_left
        for i in range(k):
            sum_left-=cardPoints[k-1-i]
            sum_right+=cardPoints[n-1-i]
            res = max(res,sum_left+sum_right)

        return res
