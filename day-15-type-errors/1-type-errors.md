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