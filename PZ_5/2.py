import math  # Импортируем модуль math для доступа к функциям exp и ln

def Power1(A, B):
    if A <= 0:
        return 0  # В случае нулевого или отрицательного параметра A функция возвращает 0
    else:
        result = math.exp(B * math.log(A))  # Вычисляем AB по формуле AB = exp(B*ln(A))
        return result
# Даны числа P, A, B, C
P = 2
A = 3
B = 4
C = 5

# Находим степени AP, BP, CP с помощью функции Power1
AP = Power1(A, P)
BP = Power1(B, P)
CP = Power1(C, P)

# Выводим результаты
print(f"Степень {A} в степени {P} равна: {AP}")
print(f"Степень {B} в степени {P} равна: {BP}")
print(f"Степень {C} в степени {P} равна: {CP}")
