# Write a code which gives grade to students according to theirs scores:

grade=float(input('Your Grade is: '))
if grade>=90 and grade<=100:
    print('Your Grade Result is: A ')
elif grade>=70 and grade<=89:
    print('Your Grade Result is: B ')
elif grade>=60 and grade<=69:
    print('Your Grade Result is: C ')
elif grade>=50 and grade<=59:
    print('Your Grade Result is: D ')
elif grade>=0 and grade<=49:
    print('Your Grade Result is: F ')