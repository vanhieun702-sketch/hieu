def longest_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().split()
        max_len = max(len(w) for w in words)
        return [w for w in words if len(w) == max_len]

# Test
print(longest_words(r"F:\TEST\amd\t.txt"))
