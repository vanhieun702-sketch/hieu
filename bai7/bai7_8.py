def write_list_to_file(filename, data_list):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data_list:
            f.write(str(item) + "\n")

# Test
write_list_to_file(r"F:\TEST\amd\t.txt", ["Python", "Java", "C++", 123])
