# Посчитайте сумму всех чисел в списке. В списке могут быть строки


l = [1, 2, 3, 'g', 'y']
l2 = []

for i, v in enumerate(l):
    if type(v) == int:
        l2.append(v)
    else:
        pass
    print('сумма чисел в строке:', sum(l2))
# rezult: сумма чисел в строке: 6
