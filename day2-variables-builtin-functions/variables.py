# Day2: 30 Days of python programming

# Level 1

# Variables

first_name="Quang Anh"
last_name="Tran"
full_name="Quang Anh Tran"
country="Viet Nam"
city="Ha Noi"
age="24"
year="2020"
is_married=False
is_true=True
is_light_on=False
person_info= {
    'firstname':'Quang Anh',
    'lastname':'Tran',
    'country':'Viet Nam',
    'city':'Ha Noi'
    }

# Printing the values stored in the Variables

print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Person information: ', person_info)

# Level 2

# Check Data type
print('first_name datatype:', type(first_name))
print('last_name datatype: ', type(last_name))
print('in_married datatype: ', type(person_info))
print('person_info: ', type(person_info))

# Print length of first_name and last_name
print('First name length:', len(first_name))
print('Last name length: ', len(last_name))

# Math 
num_one=5
print('So thu nhat la:', num_one)
num_two=4
print('So thu hai la:', num_two)
_total=num_one+num_two
_diff=num_one-num_two
_product=num_one*num_two
_division=num_one/num_two
_remainder=num_one%num_two
_exp=num_one**num_two
_floor_division=num_one//num_two
print('Tong cua So thu nhat va so thu 2 la: ',_total)
print('Hieu cua So thu nhat tru so thu 2 la:',_diff)
print('Ket qua cua So thu nhat nhan so thu 2 la: ',_product)
print('Ket qua cua So thu nhat chia so thu 2 la: ',_division)
print('So thu nhat chia so thu hai du: ',_remainder)
print('Luy thua cua So thu nhat va So thu 2 la: ',_exp)
print('Phan nguyen cua So thu nhat chia So thu 2 la:',_floor_division)

# Circle
pi=3.14
#radius=float(30)
radius=float(input('Moi nhap ban kinh hinh tron: '))
area_of_circle=pi*radius*radius
circum_of_circle=2*pi*radius
print('Dien tich hinh tron la:',area_of_circle)
print('Chu vi hinh tron la:',circum_of_circle)


# Nhap gia tri tung bien

firstname=str(input('First name: '))
lastname=str(input('Last name: '))
yourcountry=str(input('Country: '))
yourage=int(input('Your Age: '))
print('Your Personal Information: ')
print('First name: ',firstname)
print('Last name: ',lastname)
print('Country: ',yourcountry)
print('Age: ',yourage)

# Help
help(input('Moi ban nhap Keywords: '))