# Nhập các số, cách nhau bằng dấu phẩy
numbers = input("Nhập các số, cách nhau bằng dấu phẩy: ").split(',')

# Lọc các số lẻ
odd_numbers = [num for num in numbers if int(num) % 2 != 0]

# In kết quả
print("Các số lẻ:", ",".join(odd_numbers))
