#Дано вещественное число А и целое число N (>0). Используя один цикл,найти значение выражения 1-А+А(2) — А(3)+ … +(-1(N)) A(N)

a = input('введите вещественное число')
while '.' not in a:
    print('Error')
    a = input('введите вещественное число')
n = input('введите целое число')
while not n.isdigit():
    print('Error')
    n = input('Введите целое число ')
znak = -1
summ = 1
for i in range(1, int(n) +1):
    new_a = float(a) ** i
    summ += new_a * znak
    znak *= -1
print(f'сумма выражения: {summ}')
