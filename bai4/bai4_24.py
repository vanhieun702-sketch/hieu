sentence = input("Nhập một câu: ")

uppercase = sum(c.isupper() for c in sentence)
lowercase = sum(c.islower() for c in sentence)

print("Chữ hoa:", uppercase)
print("Chữ thường:", lowercase)
