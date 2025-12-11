
from math import*

a, b, c = map(int, input().split())

d = b**2 - 4*a*c

if d < 0:
    print('vn')

elif d == 0:
    print(-b/(2*a))

else:
    print((-b + sqrt(d))/(2*a))

    print((-b - sqrt(d))/(2*a))

