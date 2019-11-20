#матрица,закрутить по часовой стрелке(надо сделать так):
# 1 2 3        1 2 3
# 8 9 4   из   4 5 6
# 7 6 5        7 8 9

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range (len(m)):
        if i == 0:
                print('1:',m[i][0],m[i][1],m[i][2])

for i in range (len(m)):
    for j in range(len(m)):
        if i == 1:
                if j == 2:
                        print('2:',m[j][1],m[j][2],m[i][0])

for i in range (len(m)):
    for j in range(len(m)):
        if i == 1:
                if j ==  2:
                        print('3:',m[j][0],m[i][2],m[i][1])

#rezult:  1: 1 2 3
#rezult:  2: 8 9 4
#rezult:  3: 7 6 5
