# Проверьте, повторяются ли символы в строке

l = [1,2,3,5,3,4,7]
m = (list(set(l)))
if l == m:
    print('повторяющихся элементов нет')
else:
    print('повторяющиеся элементы есть')
