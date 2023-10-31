# Даны три целых числа,одно из которых отлично от двух других,равных между собой .Определить порядковый номер числа,отличного от остальных
try:
    a, b, c = int(input()), int(input()), int(input())
    if a == b != c:
        print('3')
    elif a != b == c:
        print('1')
    elif a != b != c:
        print('Ошибка')
    else:
        b == c != a
        print('2')
except:
    print('В')