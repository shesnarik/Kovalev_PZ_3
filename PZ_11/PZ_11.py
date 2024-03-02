
numbers = [1, -2, 3, -4, 5, -6]

positive_numbers = [str(num) for num in numbers if num > 0]
negative_numbers = [str(num) for num in numbers if num < 0]

with open('ale.txt', "w", encoding='utf-8') as file:
    file.write(f'{" ".join(positive_numbers)}\n{" ".join(negative_numbers)}')

with open('ale.txt', "r", encoding='utf-8') as file:
    ale = file.readlines()
positive_numbers = ale[0].strip().split()
negative_numbers = ale[1].split()
with open("numbers.txt", "w", encoding='utf-8') as file:
    file.write(f"Количество элементов: {len(positive_numbers) + len(negative_numbers)}\n")
    file.write(f"Положительные числа: {', '.join(positive_numbers)}\n")
    file.write(f"Количество положительных чисел: {len(positive_numbers)}\n")
    file.write(f"Отрицательные числа: {', '.join(negative_numbers)}\n")
    file.write(f"Количество отрицательных чисел: {len(negative_numbers)}\n")
