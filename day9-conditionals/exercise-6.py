fruits = ['banana', 'orange', 'mango', 'lemon']
fruit=input('Your fruit want to know is: ')
exist=fruit in fruits
if exist==True:
    print('Your fruit is already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)