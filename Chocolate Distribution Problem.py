from math import inf

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        # sort first
        A.sort()
        l = 0
        minimum = float(inf)
        
        for r in range(M-1,N):
            if A[r]>=A[l]:
                minVal = A[r]-A[l]
                minimum = min(minimum,minVal)
                r += 1
                l += 1
        return minimum
