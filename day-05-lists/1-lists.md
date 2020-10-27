# Lists in Python

Có 4 kiểu để thu thập dữ liệu trong Python:

- **List**: là một tập hợp được sắp xếp theo thứ tự và có thể thay đổi (modifiable). Cho phép các thành viên trùng lặp.

- **Tuple**: là một tập hợp được sắp xếp theo thứ tự và không thể thay đổi hoặc không thể thay đổi (bất biến). Cho phép các thành viên trùng lặp.

- **Set**: là một bộ sưu tập không có thứ tự, không được lập chỉ mục và không thể sửa đổi, nhưng bạn có thể thêm các mục mới. Không có thành viên trùng lặp.

- **Dictionary**: là một tập hợp không có thứ tự, có thể thay đổi (có thể sửa đổi) và được lập chỉ mục. Không có thành viên trùng lặp.

**List** là tập hợp các kiểu dữ liệu khác nhau được sắp xếp theo thứ tự và có thể sửa đổi (có thể thay đổi). Một danh sách có thể trống hoặc nó có thể có các mục hoặc mục kiểu dữ liệu khác nhau.

## How to Create a List - Cách tạo một List trong Python

Có hai cách để tạo một List:

- Sử dụng built-in functiong:

```
# syntax
lst = list()
```

```
empty_list = list() # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

- Sử dụng dấu ngoặc vuông `[]`

```
# syntax
lst = []
```

```
empty_list = [] # this is an empty list, no item in the list
print(len(empty_list)) # 0
```

Chúng ta cũng có thể sử dụng lệnh len() để kiểm tra độ dài của một List.

```
fruits = ['banana', 'orange', 'mango', 'lemon']                     # list of fruits
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

Kết quả:

```
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

Trong một List có thể có nhiều loại dữ liệu khác nhau:

` lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}]`

## Accessing List Items Using Positive Indexing

Chúng ta có thể lấy dữ liệu một List bằng cách truy cập vào từng ví trị của dữ liệu đó trong danh sách. Dữ liệu đầu tiên trong List bắt đầu từ vị trí 0. Ví dụ:

<img src="https://imgur.com/FmbFbkE.png">

```
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # we are accessing the first item using its index
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# Last index
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

## Accessing List Items Using Negative Indexing

Chúng ta cũng có thể lấy dữ liệu trong List bằng cách lấy từ vị trí ngược lại. Dữ liệu cuối cùng trong List sẽ bắt đầu từ `-1` Ví dụ:

<img src="https://imgur.com/mwdSyqg.png">

```
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

## Unpacking List Items

```
lst = ['item','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

```
# First Example
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = lst
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# Second Example about unpacking list
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

## Slicing Items from a List

Cũng giống như việc lấy dữ liệu trong List bằng vị trí của dữ liệu đó, chúng ta cũng có thể lấy một loạt dữ liệu trong List bằng cách đánh đấu bắt đầu lấy từ vị trí nào đến vị trí nào đó.

- Positive Indexing:

```
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # it returns all the fruits
# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['orange', 'lemon']
```

- Negative Indexing:

```
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index
orange_mango_lemon = fruits[-3:] # this will give the same result as the one above
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order
```

## Modifying Lists

Chúng ta cũng có thể thay đổi dữ liệu trong List bằng cách sử dụng vị trí của dữ liệu ta muốn thay đổi.

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

## Checking Items in a List

Kiểm tra một dữ liệu có xuất hiện trong List không.

```
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

## Adding Items to a List

Chúng ta có thể thêm dữ liệu vào một List đã tồn tại, dữ liệu đó sẽ bắt đầu từ vị trí cuối cùng trong List. Ta sử dụng lệnh `append()`:

```
# syntax
lst = list()
lst.append(item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

## Inserting Items to a List

Chúng ta cũng có thể thêm một dữ liệu vào một vị trí trong List chứ không nhất thiết phải là vị trí cuối cùng như việc thêm dữ liệu vào List. Ta sử dụng lệnh `insert()`:

```
# syntax
lst = ['item1', 'item2']
lst.insert(index, item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

## Removing Items from a List

Ta sử dụng lệnh `remove()` để xóa một dữ liệu chỉ định trong List:

```
# syntax
lst = ['item1', 'item2']
lst.remove(item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurence of the item in the list
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

## Removing Items Using Pop

Lệnh `pop()` cũng được sử dụng để xóa một dữ liệu trong List (Nếu như lệnh để trống sẽ mặc định xóa dữ liệu cuối cùng):

```
# syntax
lst = ['item1', 'item2']
lst.pop()       # last item
lst.pop(index)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

## Removing Items Using Del

Sử dụng lệnh `del` để xóa một dữ liệu chỉ định hoặc một dải dữ liệu trong List. Lệnh `del` cũng có thể sử dụng để xóa hoàn toàn dữ liệu trong một List.

```
# syntax
lst = ['item1', 'item2']
del lst[index] # only a single item
del lst        # to delete the list completely
```

```
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # this deletes items between given indexes, so it does not delete the item with index 3!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # This should give: NameError: name 'fruits' is not defined
```

## Clearing List Items

Lệnh clear() dùng để xóa hoàn toàn dữ liệu trong một List:

```
# syntax
lst = ['item1', 'item2']
lst.clear()
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

## Copying a List

Có thể sao chép một danh sách bằng cách gán lại nó cho một biến mới theo cách sau: list2 = list1. Bây giờ, list2 là một tham chiếu của list1, bất kỳ thay đổi nào chúng ta thực hiện trong list2 cũng sẽ sửa đổi bản gốc, list2. Nhưng có rất nhiều trường hợp mà chúng ta không muốn sửa đổi bản gốc thay vào đó chúng ta muốn có một bản sao khác. Một trong những cách tránh vấn đề trên là sử dụng copy ().

```
# syntax
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

## joining Lists

Có nhiều cách để kết nối 2 hay nhiều Lists với nhau trong Python.

- Sử dụng toán tử (+)

```
# syntax
list3 = list1 + list2
```

```
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables )
```

Kết quả:

```
# output
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

- Nối Lists bằng lệnh extend():

```
# syntax
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2)
```

```
num1 = [0, 1, 2, 3]
num2= [4, 5,6]
num1.extend(num2)
print('Numbers:', num1)
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers)
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits )
```

Kết quả:

```
Numbers: [0, 1, 2, 3, 4, 5, 6]
Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

## Counting Items in a List

Sử dụng lệnh count() để kiểm tra số lượng một dữ liệu xuất hiện trong một List:

```
# syntax
lst = ['item1', 'item2']
lst.count(item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

## Finding Index of an Item

Lệnh index() để xuất ra dữ liệu cần tìm trong một List:

```
# syntax
lst = ['item1', 'item2']
lst.index(item)
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, the first occurrence
```

## Reversing a List

Lệnh `reverse()` đảo ngược ví trí của các dữ liệu trong List.

```
# syntax
lst = ['item1', 'item2']
lst.reverse()
```

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits.reverse())
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages.reverse())
```

Kết quả:

```
['lemon', 'mango', 'orange', 'banana']
[24, 25, 24, 26, 25, 24, 19, 22]
```

## Sorting List Items

Để sắp xếp danh sách chúng ta có thể sử dụng phương thức sort () hoặc các hàm dựng sẵn sorted (). Phương thức sort () sắp xếp lại các mục trong danh sách theo thứ tự tăng dần và sửa đổi danh sách ban đầu. Nếu một đối số của phương thức sort () đảo ngược bằng true, nó sẽ sắp xếp danh sách theo thứ tự giảm dần.

- `sort()`: Lệnh này được sử dụng sẽ thay đổi luôn List nguyên bản

```
# syntax
lst = ['item1', 'item2']
lst.sort()                # ascending
lst.sort(reverse=True)    # descending
```

Ví dụ:

```
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order
fruits.sort(reverse=True)
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)
```

Kết quả:

```
['banana', 'lemon', 'mango', 'orange']
['orange', 'mango', 'lemon', 'banana']
[19, 22, 24, 24, 24, 25, 25, 26]
[26, 25, 25, 24, 24, 24, 22, 19]
```

- `sorted()`: Lệnh này sử dụng sẽ không làm thay đổi List nguyên bản

```
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))     # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
```