#Даны три целы числа : A,B,C. Проверить истинность высказывания : "Ровно два из чисел А,В,С являются положительными".
try:
    A, B, C = int(input("введите первое число ")), int(input("введите второе число ")), int(input("введите третье число "))
    if (A > 0 and B > 0) or (C > 0 and B > 0) or (A > 0 and C > 0):
        print('true')
    else:
        print('false')
except:
    print("error")