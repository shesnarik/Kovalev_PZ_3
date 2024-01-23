original_dict = {i: i**2 for i in range(7)}
print("Исходный словарь")
print(original_dict)
keys_to_remove = [1,2]
for key in keys_to_remove:
    original_dict.pop(key)
print(original_dict)
