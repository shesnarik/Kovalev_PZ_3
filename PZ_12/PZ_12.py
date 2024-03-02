#.В последовательности на n целых чисел умножить все элементы на первый элемент.

numbers = [2, 4, 6, 8, 10]
multiplied_numbers = list(map(lambda x: x * numbers[0], numbers))
print(multiplied_numbers)