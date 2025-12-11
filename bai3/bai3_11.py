
from math import*
#x là lãi đơn
#y là kì 
#z là vốn
x, y, z = map(int, input().split())
def benefit(n,t,k):
    return k*(1+n*(t/100))


print(benefit(x,y,z))

