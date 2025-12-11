
input_f = open('F:/TEST/amd/t.txt', 'r')
for line in input_f:
    l = len(line)
    s = ' '
    while (l >= 1):
        s += line [l - 1]
        l = l -1
    print (s)

input_f.close()