# Найдите и выведите наиболее и наимее часто встречающеся слова в строке

l = ['ау','мохнатый', 'шмель', 'на', 'мохнатый', 'хмель','шмель','мохнатый','цапля']
l2 = []

for i, v in enumerate(l):
    for i2, v2 in enumerate(l):
        if i != i2 and v == v2:
            l2.append(v)
        else:
            pass
print('1й проход:',l2)
#rezult - 1й проход: ['мохнатый', 'мохнатый']

for i, v in enumerate(l2):
    for i2, v2 in enumerate(l2):
        if i != i2 and v == v2:
            v = v2
        else:
            pass
print('повторяющееся слово:', v)
#rezult - повторяющееся слово: мохнатый
