# Sets in Python

Định nghĩa Toán học của một Set (Tập hợp) có thể được áp dụng trong Python. Set là một tập hợp chứa các phần tử riêng biệt và không có thứ tự. Trong Python Set được sử dụng để chứa các giá trị độc nhất, ta có thể tìm được *intersection, difference, symmetric difference, subset, super set và disjoint set* trong Sets.

## Creating a Set

Để tạo một Set, ta sử dụng dấu ngoặc nhọn `{}`

- Tạo một Set rỗng:

```
# syntax
st = {}
# or
st = set()
```

- Tạo một Set chứa các giá trị:

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

Ví dụ:

```
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

## Getting Set's Length

Chúng ta sử dụng lệnh `len()` để kiểm tra độ dài của một Set.

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(set)
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

## Accessing Items in a Set

Chúng tôi sử dụng vòng lặp để truy cập các giá trị. Chúng ta sẽ thấy điều này trong phần vòng lặp (loop)

## Checking an Item

Kiểm tra một giá trị có trong Set hay không, ta sử dụng lệnh `in`.

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
'mango' in fruits
```

## Adding Items to a Set

Khi Set được tạo ra ta không thể thay đổi các giá trị bên trong nhưng có thể thêm giá trị vào.

- Để thêm giá trị ta sử dụng lệnh `add()`

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

- Thêm nhiều giá trị vào Set ta sử dụng lệnh `update()`

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

## Removing Items from a Set

Chúng ta có thể xóa một giá trị trong Set bằng cách sử dụng lệnh `remove()`. Nếu một giá trị không được tìm thấy khi sử dụng lệnh `remove()` thì sẽ báo lỗi, nên trước tiên ta phải kiểm tra giá trị đó có tồn tại trong Set không. Tuy nhiên, lệnh `discard()` sẽ không xuất hiện thông báo lỗi.

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes the last element from the set
```

## Clearing Items in a Set

Nếu chúng ta muốn xóa toàn bộ các giá trị trong một Set, ta sử dụng lệnh `clear`

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

## Deleting a Set

Nếu chúng ta xóa hẳn một Set, ta sử dụng lệnh `del`

```
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del set
```

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

## Converting List to Set

Chúng ta cũng có thể chuyển một List sang Set và ngược lại. Nếu ta chuyển từ List sang Set thì sẽ xóa các giá trị trùng lặp nhau và sẽ chỉ có các giá trị độc lập duy nhất.

```
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
```

Ví dụ:

```
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

## Joining Sets

Chúng ta có thể kết nối 2 Sets với nhau bằng lệnh `union()` hoặc `update()`

- Lệnh `union()` sẽ kết hợp 2 Sets và tạo ra một Set mới

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

- Lệnh `update()` sẽ thêm giá trị của Set vào trong một Set cũ

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
```

Ví dụ:

```
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

## Finding Intersection Items

Lệnh `intersection` sẽ cho chúng ta biết các giá trị cũng xuất hiện trong các Sets.

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
```

Ví dụ:

```
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
```

## Checking Subset and Super Set

- Subset: issubset()

- Super set: issuperset

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

Ví dụ:

```
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

## Checking the Difference Between Two Sets

Sử dụng lệnh `difference` để biết những giá trị không xuất hiện trong cả 2 Sets.

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
```

Ví dụ:

```
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
```

## Finding Symmetric Difference Between Two Sets

Lệnh `symmetric_difference` để kiểm tra sự điểm bất đối xứng giữa 2 Sets. Lệnh này sẽ tạo ra một Set mới có các giá trị của 2 Sets ngoại trừ các giá trị trùng lặp nhau giữa 2 Sets. Công thức trong Toán học là (A\B) ∪ (B\A)

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B)
st2.symmetric_difference(st1) # {'item1', 'item4'}
```

Ví dụ:

```
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
```

## Joining Sets

Nếu 2 Sets không có chung một hoặc nhiều giá trị ta gọi đó là *disjoint sets*. Chúng ta có thể kiểm tra 2 Sets được gọi là *joint* hoặc *disjoint* bằng cách sử dụng lệnh `isdisjoint()`

```
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

Ví dụ:

```
even_numbers = {0, 2, 4 ,6, 8}
even_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
```