# Tuples in Python

**Tuple** là một kiểu thu thập dữ liệu không thể thay đổi (immutable). Tuple được viết bằng cách sử dụng dấu ngoặc tròn `()`. Khi một Tuple được tạo ra, chúng ta không thể thay đổi giá trị trong đó. Chúng ta không thể sử dụng những chức năng thêm, chèn, xóa vì Tuple không thể sửa đổi. Khác với **List**, **Tuple** có một vài lệnh như sau:

- tuple(): Tạo một Tuple trắng, không có giá trị nào.

- count(): Đếm những giá trị được tạo trong một Tuple.

- index(): Tìm giá trị trong một Tuple.

- operator: Nối một hoặc nhiều Tuples với nhau để tạo một Tuple mới.

## Creating a Tuple

- Tuple trắng: Tạo một Tuple không chứa giá trị.

```
# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
```

- Tạo một Tuple có chứa giá trị:

```
# syntax
tpl = ('item1', 'item2','item3')
```

`fruits = ('banana', 'orange', 'mango', 'lemon')`

## Tuple length

Sử dụng lệnh `len()` để kiểm tra độ dài của một Tuple

```
# syntax
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

## Accessing Tuple Items

Cũng giống như **List**, chúng ta có thể lấy giá trị tại vị trí chỉ định theo 2 cách:

- Positive Indexing: Vị trí của giá trị đầu tiên là `0`.

<img src="https://imgur.com/RCHQjB7.png">

```
# Syntax
tpl = ('item1', 'item2', 'item3')
first_item = tpl[0]
second_item = tpl[1]
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[0]
second_fruit = fruits[1]
last_index =len(fruits) - 1
last_fruit = fruits[las_index]
```

- Negative Indexing: Giá trị cuối cùng là `-1` và đếm lùi theo số âm.

<img src="https://imgur.com/9xDJbqP.png">

```
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
first_item = tpl[-4]
second_item = tpl[-3]
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
first_fruit = fruits[-4]
second_fruit = fruits[-3]
last_fruit = fruits[-1]
```

## Slicing Tuples

Chúng ta có thể cắt một đoạn các giá trị bằng cách sử dụng một giải giá trị Positive Indexing hoặc là Negative Indexing. Các giá trị trả về sau khi ta lấy ra từ Tuple sẽ trở thành một Tuple mới.

- Dải giá trị Positive Indexing:

```
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[0:4]    # all items
all_fruits= fruits[0:]      # all items
orange_mango = fruits[1:3]  # doesn't include item at index 3
orange_to_the_rest = fruits[1:]
```

- Dải giá trị Negative Indexing:

```
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]    # all items
orange_mango = fruits[-3:-1]  # doesn't include item at index 3
orange_to_the_rest = fruits[-3:]
```

## Changing Tuples to Lists

Chúng ta có thể thay đổi Tuples sang Lists hoặc từ Lists sang Tuples. Vì Tuple không thể thay đổi các giá trị nên ta sẽ phải chuyển Tuple sang List nếu muốn thay đổi.

```
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

## Checking an Item in a Tuple

Chúng ta có thể kiểm tra một giá trị có trong Tuple hay không, kết quả trả về `True or False`.

```
# Syntax
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

## Joining Tuples

Chúng ta có thể kết nối hai hoặc nhiều Tuples với nhau bằng toán tử `+`.

```
# syntax
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

## Deleting Tuples

Cũng giống như List, ta sử dụng lệnh `del` để xóa một Tuple

```
# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

```
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```