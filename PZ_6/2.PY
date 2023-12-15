a = [4, 1, 235, 7, 64, 454, 1, 234, 75, 22, 56]
min_index = None
max_index = None
for i in a:
    if a.count(i) == 2:
        min_index = a.index(i)
        new_a = a[min_index + 1:]
        max_index = min_index + 1 + new_a.index(i)
print(min_index)
print(max_index)