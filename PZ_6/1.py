a = [4, 1, 235, 7, 64, 454, 46436, 234, 75, 22, 56]
n = len(a)
print(a[0])
print(a[1])
print(a[n - 1])
print(a[n - 2])
print(a[2])
print(a[3])
for i in range(-3, -(n + 1), -1):
    print(a[i])