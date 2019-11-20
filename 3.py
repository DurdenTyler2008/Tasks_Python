# Удалите дубликаты из списка
l = [1,2,2,3,5,7,6,5,9,8,9]

n = len(l)

for j in range(0, n-1):
    for i in range(0, n-1-j):
        if l[i] > l[i + 1]:
            l[i],l[i + 1] = l[i +1],l[i]
print('сортированный список:', l)
#result:сортированный список: [1, 2, 2, 3, 5, 5, 6, 7, 8, 9, 9]

newl = []
for i in l:
    if i not in newl:
        newl.append(i)

print('список без дубликатов:', newl)
#result:список без дубликатов: [1, 2, 3, 5, 6, 7, 8, 9]
