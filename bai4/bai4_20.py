from math import comb

n = int(input("Nhập n: "))

for i in range(n):
    row = [str(comb(i, j)) for j in range(i+1)]
    print(' '.join(row))
