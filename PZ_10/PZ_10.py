#Три цветовода выращивают розы. Определить, какие из известных сортов роз «Анжелика»,
#«Виктория», «Гагарин», «Катарина», «Юбилейная», «Южная» имеются у каждого
#цветоводы, есть хотя бы у одного из цветоводов и каких нет ни у одного из цветоводов.
colorist_A = {"Анжелика", "Гагарин", "Южная"}
colorist_B = {"Виктория", "Катарина", "Юбилейная"}
colorist_C = {"Виктория", "Гагарин", "Катарина"}

roses_intersection = colorist_A & colorist_B & colorist_C
if len(roses_intersection) == 0:
    print("ошибка")
else:
    print("Сорта роз, которые есть у каждого цветовода:", roses_intersection)


roses_union = colorist_A | colorist_B | colorist_C
if len(roses_union) == 0:
    print("Ошикба")
else:
    print("Сорта роз, которые есть хотя бы у одного цветовода:", roses_union)

roses_not_in_any = {"Анжелика", "Виктория", "Гагарин", "Катарина", "Юбилейная", "Южная"} - roses_union
if len(roses_not_in_any) == 0:
    print("Ошибка")
else:
    print("Сорта роз, которые нет ни у одного цветовода:", roses_not_in_any)

