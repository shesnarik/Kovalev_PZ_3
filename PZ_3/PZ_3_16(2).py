# Даны три целых числа,одно из которых отлично от двух других,равных между собой .Определить порядковый номер числа,отличного от остальных

try:
    a, b, c = int(input()), int(input()), int(input())
    if a == b != c:
        print('3')
    elif a != b == c:
        print('1')
    elif a != b != c:
        print('2')
    else:
        b == c != a
        print('Ошибка')
except:
    print('В')