# https://leetcode.com/problems/3sum/

# B R U T E F O R C E

def triplet(a):
    result = set() # to avoid duplicates
    n = len(a)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (a[i]+a[j]+a[k])==0:
                    temp = [a[i],a[j],a[k]]
                    temp.sort() #sorted so that there will be no duplicates added to the set
                    result.add(tuple(temp)) # if not made tuple, then it will show error that list is not hashable
    ans = [list(item) for item in result]
    return ans

arr = [-1, 0, 1, 2, -1, -4]

print(triplet(arr))

# B E T T E R A P P R O A C H

# Instead of using a third loop to take the third element, we use hashmap.
# To prevent taking the same element in a group again, we store the elements in between i and j only in a hashSet
def triplet(a):
    n = len(a)
    ans = set()
    for i in range(n):
        hashSet = set()
        for j in range(i+1,n):
            third = -(a[i]+a[j])
            if third in hashSet:
                temp = [a[i], a[j], third]
                temp.sort()
                ans.add(tuple(temp))
            hashSet.add(a[j])
    result = list(ans)
    return result


arr = [-1, 0, 1, 2, -1, -4]
print(triplet(arr))


# O P T I M A L A P P R O A C H
class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        n = len(a)
        ans = []
        a.sort()
        for i in range(n):
            if i != 0 and a[i] == a[i - 1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                totalsum = a[i]+a[j]+a[k]
                if(totalsum<0):
                        j+=1
                elif(totalsum>0):
                        k-=1
                else:
                    temp = [a[i],a[j],a[k]]
                    ans.append(temp)
                    j=j+1
                    k=k-1
                    while(j<k and a[j]==a[j-1]):
                        j+=1
                    while(j<k and a[k]==a[k+1]):
                        k-=1
        return ans

# We avoided the use of the 2 hashsets. Instead used 2 pointer method
