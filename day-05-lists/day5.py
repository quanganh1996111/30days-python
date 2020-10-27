empty_list=[]
list1=['Anh Tran Quang', 24, 'Viet Name', 'Male', True, 'IT Engineer']
print(len(list1))
first, second, third, fourth, fiveth, sixth = list1
print(first)
print(third)
print(sixth)
mixed_data_types=['Tran Quang Anh', 24, '175cm', False, 'Ha Noi']
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(mixed_data_types)
print(len(it_companies))
print(it_companies[0], it_companies[2], it_companies[6])
it_companies[6]='Nhan Hoa'
print(it_companies)
it_companies.append('Amazon')
print(it_companies)
it_companies.insert(3, 'Tencent')
cap=it_companies[3]
x=cap.upper()
print(x)
it_companies_result='#; '.join(it_companies)
print(it_companies_result)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first3_companies=it_companies[0:3]
last3_companies=it_companies[-4:-1]
print(first3_companies)
print(last3_companies)
it_companies.pop(0)
print(it_companies)
it_companies.pop(3)
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies