print('Exercise 1: ')

count = 0
while count < 11:
    print(count)
    count = count + 1

print('Exercise 2: ')
numbers = (0,1,2,3,4,5,6,7,8,9,10)
for number in numbers:
    print(number)

print('Exercise 3: ')

def pypart(n): 
    myList = [] 
    for i in range(1,n+1): 
        myList.append("# "*i) 
    print("\n".join(myList)) 

n = 7
pypart(n)

print('Exercise 4: ')

num_rows = 7
num_cols = 7

for i in range(num_rows):
    print('# ', end=' ')
    for j in range(num_cols-1):
        i*=j
        print('# ', end=' ')
    print('')