a = [4, 1, 235, 7, 64, 454, 1, 234, 75, 22, 56]
k = 3
for _ in range(k):
    for i in range(len(a)):
        a[0], a[i] = a[i], a[0]
print(a)