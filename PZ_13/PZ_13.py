matrix = [[i+j for j in range(3)] for i in range(0, 7, 3)]
sums = [sum(row) for row in matrix]

for i in range(len(matrix)):
    matrix[i][2] = sums[i]
for row in matrix:
    print(row)