# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
your_age=int(input('Enter your age: '))
if your_age >= 18:
    print('You are old enough to learn to drive.')
elif your_age < 18:
    print('You need 3 more years to learn to drive.')

# 2. 

my_age=int(input('My Age is: '))
age1=my_age-your_age
age2=your_age-my_age
if your_age < my_age:
    if age1<1:
        print('You are', age1, 'year younger than me.')
    else:
        print('You are', age1, 'years younger than me.')
if your_age > my_age:
    if age2<1:
        print('You are', age2, 'year older than me.')
    else:
        print('You are', age2, 'years older than me.')
if your_age==my_age:
    print('You and me are the same age.')