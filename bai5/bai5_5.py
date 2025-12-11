from bai5_6 import sort_list, find_max

# nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

lst = []

# nhập giá trị list
for i in range(n):
    val = float(input(f"Nhập giá trị thứ {i+1}: "))
    lst.append(val)

# sắp xếp
sorted_list = sort_list(lst)

# tìm max bằng module
max_value = find_max(lst)

# tìm min không cần module (được phép dùng min)
min_value = min(lst)

print("\nDanh sách ban đầu:", lst)
print("Danh sách sau khi sắp xếp:", sorted_list)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
