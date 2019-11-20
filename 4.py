# Сделайте проверку, явдяется ли слово Палиндромом

word = str(input('введите слово:'))
x = len(word)
i = 0
k = 0
x = x - 1

while x - i >= i:
    if word[x - i] == word[i]:
        i = i + 1
    else:
        k = 1
        break
if k == 1:
    print('нет,это не палиндром')
else:
    print('да,это палиндром')
