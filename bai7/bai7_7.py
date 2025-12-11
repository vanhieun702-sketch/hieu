def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


print("Số dòng:", count_lines(r"F:\TEST\amd\t.txt"))
