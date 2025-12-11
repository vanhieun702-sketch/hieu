
hoten = input().strip()
tach = hoten.split()
if len(tach) == 2:
    ho = tach[0]
    ten = tach[1]
    print("Họ:", ho)
    print("Tên:", ten)
else:
    print("Vui lòng nhập đúng định dạng: Họ Tên (chỉ 2 từ)")
