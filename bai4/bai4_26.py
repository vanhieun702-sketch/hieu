balance = 0  # Khởi tạo số dư ban đầu

print("Nhập các giao dịch, mỗi giao dịch 1 dòng. Nhập 'STOP' để kết thúc:")

while True:
    transaction = input()
    if transaction.upper() == "STOP":
        break
    
    action, amount = transaction.split()
    amount = int(amount)
    
    if action.upper() == "D":
        balance += amount  # Nạp tiền
    elif action.upper() == "W":
        balance -= amount  # Rút tiền

print("Số tiền thực của tài khoản:", balance)
