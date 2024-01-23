a = input('Введите целое число: ')
while not a.isdigit():
    print('Error')
    a = input('Введите целое число: ')
b = input('введите целое число:')
while not b.isdigit():
    print('Error')
    b = input('введите целое число')
summ = 0
for i in range(0, int(a), int(b) + 1):
    summ += 1
print(f'колличество отрезков Б,размещенных на отрезке А: {summ}')