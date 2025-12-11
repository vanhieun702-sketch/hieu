T = open('F:/TEST/amd/t.txt', 'r')
char, wc, lc = 0, 0, 0

for line in T:
    for k in range(0, len(line)):
        char +=1
        if line[k] == ' ':
            wc += 1
        if line[k] == '\n':
            wc, lc = wc + 1, lc + 1

print (" The no.of char is %d\n The no.of words is %d\n The noof lines is %d" % ( char, wc, lc))