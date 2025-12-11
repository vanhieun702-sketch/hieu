binary_str = input("Nhập các số nhị phân 4 chữ số, phân tách bằng dấu phẩy: ")
binary_list = binary_str.split(',')

# Lọc các số chia hết cho 5
div5 = [b for b in binary_list if int(b, 2) % 5 == 0]

print("Các số chia hết cho 5:", ",".join(div5))
