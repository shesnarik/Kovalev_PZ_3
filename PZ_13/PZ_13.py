#В матрице найти суммы элементов каждой строки и поместить их в новый массив.
#Выполнить замену элементов третьего столбца исходной матрицы на полученные
#cуммы.
import numpy as np

matrix = np.random.randint(1, 10, (3, 3))
print("Исходная матрица:")
print(matrix)

row_sums = np.sum(matrix, axis=1)
print("\nСуммы элементов каждой строки:")
print(row_sums)

matrix[:, 2] = row_sums
print("\nМатрица после замены элементов третьего столбца:")
print(matrix)