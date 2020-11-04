def even(x):
    count = 0
    a = range(x)
    for num in a:
        if num % 2 == 0:
            count += 1
            print(num)
    print('Dem: ',count)
def odd(x):
    count = 0
    b = range(x)
    for number in b:
        if number % 2 != 0:
            count += 1
            print(number)
    print('Dem: ',count)
x = int(input('Range: '))
even(x)
odd(x)