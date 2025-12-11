even_numbers = []

for num in range(1000, 3001):
    if all(int(d) % 2 == 0 for d in str(num)):
        even_numbers.append(str(num))

print(",".join(even_numbers))
