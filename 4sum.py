# https://leetcode.com/problems/4sum/description/

# B R U T E F O R C E M E T H O D

def four_sum(a,target):
    n = len(a)
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if a[i]+a[j]+a[k]+a[l]==target:
                        temp = [a[i],a[j],a[k],a[l]]
                        temp.sort()
                        ans.add(tuple(temp))
    st = [list(x) for x in ans]
    return st

nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
print(four_sum(nums,target))



# B E T T E R A P P R O A C H

# Instead of looping to find the 4th element, used hashSet
def four_sum(a,target):
    n = len(a)
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            hashSet = set()
            for k in range(j+1,n):
                total_sum = a[i] + a[j] + a[k]
                val = target - total_sum
                if val in hashSet:
                    temp = [a[i],a[j],a[k],val]
                    temp.sort()
                    ans.add(tuple(temp))
                hashSet.add(a[k])
    ans = list(ans) 
    return ans




nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
print(four_sum(nums,target))

# O P T I M A L A P P R O A C H
class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        n = len(a)
        result = []
        a.sort()

        for i in range(n):
            if i>0 and a[i]==a[i-1]:
                continue
            for j in range(i+1,n):
                if j>i+1 and a[j]==a[j-1]:
                    continue
                k = j+1
                l = n-1
                while k<l:
                    sum = a[i]+a[j]+a[k]+a[l]
                    if sum<target:
                        k+=1
                    elif sum>target:
                        l-=1
                    else:
                        temp = [a[i],a[j],a[k],a[l]]
                        result.append(temp)
                        k+=1
                        l-=1
                        while k<l and a[k]==a[k-1]:
                            k+=1
                        while k<l and a[l]==a[l+1]:
                            l-=1
        return result




nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
print(four_sum(nums,target))
