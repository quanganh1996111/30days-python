num = list(range(11))
for i in num:
    for j in range(0, 11):
        if i == j:
            print(i, 'x',j, '=', i*j)