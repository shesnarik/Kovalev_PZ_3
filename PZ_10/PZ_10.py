# Создаем множества для каждого цветовода
colorist_A = {"Анжелика", "Гагарин", "Южная"}
colorist_B = {"Виктория", "Катарина", "Юбилейная"}
colorist_C = {"Виктория", "Гагарин", "Катарина"}

roses_intersection = colorist_A & colorist_B & colorist_C
print("Сорта роз, которые есть у каждого цветовода:", roses_intersection)

roses_union = colorist_A | colorist_B | colorist_C
print("Сорта роз, которые есть хотя бы у одного цветовода:", roses_union)

roses_not_in_any = {"Анжелика", "Виктория", "Гагарин", "Катарина", "Юбилейная", "Южная"} - roses_union
print("Сорта роз, которые нет ни у одного цветовода:", roses_not_in_any)

