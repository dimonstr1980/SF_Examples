labirint = []
with open("labirint.txt") as myFile:
    for line in myFile:
        labirint.append(line.replace('\n', '').split(' '))

ii = 0

for i in labirint:
    jj = 0
    for j in i:
        if j == 'A':
            labirint[ii][jj] = 1
            pozln = (ii, jj)
        elif j == 'B':
            labirint[ii][jj ] = 0
            pozOut = (ii, jj)
        elif j == '1':
            labirint[ii][jj] = -1
        else:
            labirint[ii][jj] = 0
        jj += 1
    ii += 1

if not found(labirint, pozOut):
    print("Путь не найден!")
else:
    result = printPath(labirint, pozOut)

    for i in labirint:
        for line in i:
            print("{:^3}".format(line), end = " ")
        print()
    print(result)