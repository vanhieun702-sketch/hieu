
from math import*
s= input()
dem ={}

for i in range(len(s)):
    c = s[i]
    if c in dem:
        dem[c] += 1
    else:
        dem[c] =1

print (dem)

