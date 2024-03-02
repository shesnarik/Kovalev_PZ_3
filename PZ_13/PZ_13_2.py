#В матрице найти сумму элементов второй половины матрицы.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

second_half_sum = sum([row[-1] for row in matrix])

print(second_half_sum)
