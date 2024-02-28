import string

with open('text18-16.txt', 'r', encoding='utf-16') as file:
    data = file.readlines()
data = ''.join(data)
print(data)
print(f'Kol vo bykv: {len([char for char in data if char.isupper()])}')

with open('result_stix.txt', 'w', encoding='utf8') as file:
    for char in string.punctuation:
        data = data.replace(char, "!")
    file.write(data)