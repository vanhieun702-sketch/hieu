
def bubbleSort(nlist):
    loop = len(nlist)

    for i in range(loop - 1):        
        swapped = False
        for j in range(loop - 1 - i):
            if nlist[j] > nlist[j + 1]:
             
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        if not swapped:
            break

    return nlist
n = int(input("Nhập số phần tử n: "))

nlist = []
for i in range(n):
    val = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(val)

print("Danh sách ban đầu:", nlist)

sorted_list = bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
