dog={}
dog['name'] = 'jones'
dog['color'] = 'brown'
dog['breed'] = 'pitbull'
dog['legs'] = '4'
dog['age'] = '5'
print(dog)
student_dictionary={
    'first_name' :'Quang Anh',
    'last_name' : 'Tran',
    'gender' : 'Male',
    'age' : 24,
    'martial status' : False,
    'skills' : ['Tan gai', 'Da Bong', 'Chem gio'],
    'country' : 'Viet Nam',
    'city' : 'Ha Noi',
    'address' : {
        'street' : 'Giai Phong',
        'home number' : '28 ngo 773'
    }
}
print(len(student_dictionary))
print(student_dictionary['skills'])
student_dictionary['skills'].append(['Dep trai', 'Vui ve'])
print(student_dictionary['skills'])
keys=student_dictionary.keys()
print(keys)
values=student_dictionary.values()
print(values)
print(student_dictionary.items())
student_dictionary.pop('address')
print(student_dictionary)
del dog