# Nhập danh sách từ từ bàn phím, cách nhau bằng khoảng trắng
ds = input("Nhập các từ, cách nhau bằng khoảng trắng: ").split()

# Tìm chiều dài lớn nhất của các từ
max_len = max(len(word) for word in ds)

# Lọc ra tất cả các từ có độ dài bằng chiều dài lớn nhất
longest_words = [word for word in ds if len(word) == max_len]

# In ra kết quả
print("Các từ dài nhất:", ", ".join(longest_words))
