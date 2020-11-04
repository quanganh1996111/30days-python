num = list(range(101))
for i in num:
    if i % 2 == 0:
        print('Evens Numbers:', i)
for j in num:
    if j % 2 != 0:
        print('Odd Numbers: ', j)

num1=100
tong = 0
for e in range(0, num1+1, 1):
    tong = tong + e
    
    print(tong)
