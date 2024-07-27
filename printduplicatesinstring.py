# https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
from collections import defaultdict


s = "geeksforgeeks"

hashset = defaultdict(int)
for i in range(len(s)):
    hashset[s[i]]+=1

for items in (hashset):
    if hashset[items]>1:
        print(items)
