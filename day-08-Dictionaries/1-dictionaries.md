# Dictionaries in Python

Dictionary là một tập hợp các dữ liệu được ghép nối (key:value) không có thứ tự, có thể sửa đổi.

## Creating a Dictionary

Để tạo một Dictionary, chúng ta sử dụng dấu ngoặc nhọn `{}`.

```
# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

Ví dụ:

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
```

Dictionary cho chúng ta thấy một giá trị có thể là bất kỳ kiểu dữ liệu nào khác nhau: string, boolean, list, tuple, set hoặc là chính dictionary.

## Dictionary Length

Kiểm tra số lượng cặp `key:value` trong Dictionary

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7
```

## Accessing Dictionary Items

Chúng ta có thể xem các giá trị Dictionary bằng cách gọi `key` của giá trị đó.

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
```

Ví dụ:

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

Truy cập vào giá trị bằng `key` của nó sẽ báo lỗi nếu `key` không tồn tại. Để tránh gặp phải lỗi trước tiên ta cần kiểm xem `key` đã tồn tại chưa hoặc chúng ta có thể sử dụng lệnh `get`. Nếu lệnh trả về kết quả là `None`, tức là kiểu dữ liệu `NoneType` có nghĩa là `key` không tồn tại.

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

## Adding Items to a Dictionary

Chúng ta có thể thêm các cặp `key:value` vào Dictionary

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
```

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

## Modifying Items in a Dictionary

Chúng ta có thể sửa đổi giá trị trong Dictionary

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
```

Ví dụ:

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person['first_name'] = 'Eyob'
person['age']
```

## Checking Keys in a Dictionary

Chúng ta có thể sử dụng toán tử `in` để kiểm tra `key` tồn tại trong Dictionary

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

## Removing Key and Value Pairs from a Dictionary

- *pop(key)*: Xóa một giá trị bằng `key` tương ứng với giá trị đó.

- *popitem()*: Xóa giá trị cuối cùng trong Dictionary.

- *del*: Xóa một giá trị với `key` tương ứng.

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
```

Ví dụ:

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
```

## Changing Dictionary to a List of Items

Lệnh `items()` để thay đổi Dictionary thành List các Tuples.

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

## Clearing a Dictionary

Nếu chúng ta không muốn giá trị trong Dictionary chúng ta có thể clear bằng cách sử dụng lệnh `clear()`.

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

## Deleting a Dictionary

Nếu chúng ta không muốn sử dụng Dictionary chúng ta thể xóa nó đi

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

## Copy a Dictionary

Chúng ta có thể sao chép một Dictionary bằng lệnh `copy()`. Dùng lệnh sao chép chúng ta có thể tránh được ảnh hướng với Dictionary cũ.

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

## Getting Dictionary Kets as a List

Lệnh `keys()` cho chúng ta toàn bộ các `key` trong Dictionary thành một List

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

## Getting Dictionary Values as a List

Lệnh `values` cho chúng ta toàn bộ giá trị trong Dictionary thành một List

```
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```