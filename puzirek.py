massive = [1,6,88,95,4,375,2,6]
print('massive before sorted:', massive)
n = len(massive)

for j in range(0, n - 1):
    for i in range(0, n - j - 1):
        if massive[i] > massive[i + 1]:
            massive[i], massive[i + 1] = massive[i + 1], massive[i]
    else:
        pass

print('massive is sorted:', massive)
