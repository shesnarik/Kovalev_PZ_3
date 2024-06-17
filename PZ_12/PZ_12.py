#.В последовательности на n целых чисел умножить все элементы на первый элемент.

n = 5
first_element = 2

sequence = list(range(1, n+1))

result_sequence = list(map(lambda x: x * first_element, sequence))

print("Исходная последовательность:", sequence)
print("Результат умножения на первый элемент:", result_sequence)
