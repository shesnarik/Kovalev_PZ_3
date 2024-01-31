#Сгенерировать словарь вида {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36},
#удалить из него второй и третий элементы. Отобразить исходный и получившийся удалить из него второй и третий элементы. Отобразить исходный и получившийся
original_dict = {i: i**2 for i in range(7)}
print("Исходный словарь")
print(original_dict)
keys_to_remove = [1,2]
for key in keys_to_remove:
    original_dict.pop(key)
print(original_dict)
