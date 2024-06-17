#В матрице найти сумму элементов второй половины матрицы.
import numpy as np
matrix = np.random.randint(1, 10, (3, 3))
print(matrix)
second_half_sum = sum([row[-1] for row in matrix])

print(second_half_sum)
