def copy_file(src, dest):
    with open(src, "r", encoding="utf-8") as f1:
        with open(dest, "w", encoding="utf-8") as f2:
            f2.write(f1.read())

# Test
copy_file(r"F:\TEST\amd\t.txt", "target.txt")
