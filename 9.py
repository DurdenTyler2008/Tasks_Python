#матрица,закрутить против часовой стрелки(надо сделать так):
# 1 8 7      1 2 3
# 2 9 6  из  4 5 6
# 3 4 5      7 8 9

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range (len(m)):
    for j in range(len(m)):
        if i == 2:
                if j==0:
                        print('1:',m[j][0],m[i][1],m[i][0])

for i in range (len(m)):
    for j in range(len(m)):
        for k in range(len(m)):
            if i == 0:
                if j == 1:
                    if k == 2:
                        print('2:',m[i][1],m[k][2],m[j][2])

for i in range (len(m)):
    for j in range(len(m)):
        if i == 0:
                if j == 1:
                        print('3:',m[i][2],m[j][0],m[j][1])

#rezult: 1: 1 8 7
#rezult: 2: 2 9 6
#rezult: 3: 3 4 5
