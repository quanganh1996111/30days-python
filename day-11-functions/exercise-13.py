def tong(x):
    a = range(x)
    tong = 0
    for num in a:
        tong += num
    print(tong)
x = int(input('Range: '))
tong(x)