matrix = []
for i in range(5):
    matrix.append(list(map(int,input().split())))
x = 0
for j in range(5) :
    for i in range(5):
        if matrix[j][i] == 1 :
            print(j,i)
            if j == 0 or j == 4:
                x += 2
            elif j == 1 or j == 3:
                x += 1
            else:
                x += 0
            if i == 0 or i == 4:
                x += 2
            elif i == 1 or i == 3:
                x += 1
            else:
                x += 0

print(x)
