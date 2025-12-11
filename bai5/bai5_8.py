
n = int(input("Nhập số lượng phần tử của dlist: "))

dlist = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i}: "))
    dlist.append(x)

item = int(input("Nhập phần tử cần tìm: "))

def sequential(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:    
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    return found, pos
        

# nhập số lượng phần tử

found, pos = sequential(dlist, item)

if found:
    print(f"Phần tử {item} được tìm thấy tại vị trí {pos}")
else:
    print("Không tìm thấy phần tử trong danh sách")
