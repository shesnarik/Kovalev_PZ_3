
import re


with open('price.txt', 'r', encoding='utf-8') as file:
    content = file.read()


prices = re.findall(r'\d+ руб\. \d+ коп\.|\d+ руб\.', content)


print("Найденные цены:", prices)


print("Количество найденных цен:", len(prices))