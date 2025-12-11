
from math import*

x1, y1, x2, y2= map(int, input().split())

d1 = (x2 - x1) * ( x2 - x1)
d2 = ( y2 - y1) * (y2 - y1)

res = sqrt(d1 + d2)

print (res)

