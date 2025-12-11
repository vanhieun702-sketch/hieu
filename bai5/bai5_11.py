import numpy as np

data = np.array([
    ('James', 5, 48.5),
    ('Nail',  6, 52.5),
    ('Paul',  5, 42.1),
    ('Pit',   5, 40.11)
], dtype=[('name','U10'), ('class','i4'), ('height','f4')])

print("Dữ liệu ban đầu:")
print(data)

sorted_data = np.sort(data, order=['class', 'height'])

print("\nDữ liệu sau khi sắp xếp:")
print(sorted_data)
