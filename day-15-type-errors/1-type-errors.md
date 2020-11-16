# Python Type Errors

Trong Python nói riêng và các Ngôn ngữ lập trình nói chung, chúng ta sẽ gặp phải các lỗi khi tiến hành viết Code. Nếu như Code của chúng ta không chạy đươc, sẽ hiển thị một thông báo, chứa phản hồi với thông tin về vị trí xảy ra sự cố và loại lỗi. Đôi khi, nó cũng sẽ cung cấp cho chúng ta các đề xuất về cách khắc phục nếu có. Hiểu được các loại lỗi khác nhau trong Lập trình sẽ giúp chúng ta gỡ lỗi một cách nhanh chóng và giúp chúng ta làm tốt hơn.

## SyntaxError

Ví dụ:

```
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

Lỗi `SyntaxError` chúng ta gặp phải ở trên bởi vì chúng ta quên đóng dấu ngoặc đơn và gợi ý giải pháp khắc phục.

```
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
```

## NameError

```
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

Hàm `age` không được định nghĩa. Chúng ta chưa định nghĩa hàm `age` nhưng chúng ta đã cố gắng `print` ra nên sẽ có thông báo lỗi.

```
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

## IndexError


```
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

Trong ví dụ trên, List chỉ có giá trị từ 0 đến 4. Nên khi ta đặt giá trị ngoài `range` trên sẽ thông báo lỗi.

## ModuleNotFoundError

Ví dụ:

```
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

Lỗi trên thông báo về việc chúng ta thêm chữ `s` vào Module `math` nên sẽ có thông báo lỗi.

```
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

## AttributeError

Ví dụ:

```
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

Trong Module `math` mà ta vừa thêm vào, có chức năng số `pi` nhưng lại viết thành `PI` nên sẽ có thông báo lỗi. Lỗi này thông báo lên rằng chức năng này không tồn tại trong module đó. Cho nên ta phải thay đổi từ `PI` sang `pi`.

```
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

## KeyError

```
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

Thông báo lỗi trên khi ta viết lệnh lấy giá trị từ `key` nhưng ta đã gõ sai. Đây là một `key` không tồn tại, chúng ta cần gõ chính xác.

```
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

## TypeError

```
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

Thông báo lỗi trên cho ta thấy rằng chúng ta không thể thêm một giá trị định dạng `number` vào một `string`. Giải pháp đầu tiên là ta có thể chuyển giá trị `string` trên sang `int` hoặc `float`. Hoặc ta có thể chuyển giá trị `number` trên thành `string` (Kết quả sẽ là '43').

```
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

## ImportError

```
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

Thông báo lỗi trên là: Không có chức năng `power` trong Module `math`.

```
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

## ValueError

```
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

Trong giá trị `12a` có xuất hiện chữ `a` là dạng `string` nên ta không thể định nghĩa sang `number`.

## ZeroDivisionError

```
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

Chúng ta không thể lấy một số chia cho số 0.

## Tài liệu tham khảo thêm

https://docs.python.org/3/tutorial/errors.html