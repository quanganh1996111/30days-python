# Kiến thức cơ bản của Python

## Python Indentation

Trong Python, thụt lề sẽ tạo khối mã, điều này làm câu lệnh python sẽ báo lỗi.

<img src="https://imgur.com/uvSytVy.png">

Trong một số ngôn ngữ, nếu như thụt lề không đúng sẽ gây lỗi. Python ngược lại, chúng ta sẽ đơn giản hóa trong việc thực hiện lệnh mà không cần quan tâm đến việc thụt lề trong các câu lệnh.

## Python Comment

Trong Python cũng có Comment để giúp ta hiểu được ý nghĩa của từng dòng Code chúng ta sử dụng.

Comment trong Python bắt đầu bằng dấu `#`, Python sẽ không chạy các dòng lệnh bắt đầu bằng `#`

- Comment 1 dòng đơn lẻ:

```
# Ý nghĩa dòng lệnh 1
# Ý nghĩa dòng lệnh 2
# Ý nghĩa dòng lệnh 3
```

- Comment 1 đoạn nhiều dòng, ta sử dụng 3 ngoặc kép

```
"""
Giới thiệu ý nghĩa của Python này
"""
```

## Data Type

Một số kiểu dữ liệu phổ biến trong Python

### Number

- Integer: kiểu số nguyên (...,-3, -2, -1, 0, 1, 2, 3,...)

- Float: Số thực (..., -3.5, -2.2, -0.54, 0.0, 1.2314, 2.6, 3.0, ...)

### String

Tập hợp 1 hay nhiều ký tự dưới 1 dấu nháy đơn `('...')` hoặc nháy kép `("...")`

```
'Hello, World !'

"Welcome to Python"
```

### Booleans

Giá trị `True` hoặc `False`:

```
True #Bạn đang hát? Nếu đúng, giá trị là True
False #Bạn đang hát? Nếu sai, giá trị là False
```

### List

Để list một tập hợp dữ liệu trong Python:

```
[0, 1, 2, 3, 4, 5]  # Tất cả các phần từ cùng kiểu dữ liệu số - List number
['Banana', 'Orange', 'Mango', 'Avocado'] # Tất cả cùng kiểu dữ liệu String - List fruits
['Finland','Estonia', 'Sweden','Norway'] # Tất cả cùng kiểu dữ liệu String - List countries
['Banana', 10, False, 9.81] # Các phần tử có kiểu dữ liệu khác nhau - string, number, boolean, float
```

### Dictionary

Một python dictionary object là 1 tập hợp dữ liệu không có thứ tự ở định dạng `key:value`

`{'name':'AnhTQ', 'country':'VietNam', 'age':24, 'is_married':False}`

### Tuple

Giống như **List** nhưng không thể thay đổi các bộ giá trị sau khi chúng được tạo. Chúng là bất biến (immutable)

`('Ha Noi', 'Da Nang', 'Ho Chi Minh City')`

### Set

**Set** là một tập hợp các kiểu dữ liệu khác nhau như List và Tuple

Không giống **List** và **Tuple**, **Set** không phải 1 tập hợp các mục có thứ tự. Giống như trong toán học, Set trong python chỉ những item duy nhất.

`{3.14, 9.81, 2.7} # Thứ tự không quan trọng trong Set`

### Check Data Types

Sử dụng lệnh `type` để kiểm tra một dữ liệu nào đó thuộc kiểu dữ liệu nào

<img src="https://imgur.com/IbhuzVm.png">

## Chạy một file Python

Sử dụng Windows PowerShell:

- Kiểm tra version Python:

```
PS C:\Users\Quang Anh> python --version
Python 3.7.9
```

- Truy cập đến đường dẫn lưu file Python muốn chạy:

```
PS C:\Users\Quang Anh> cd 'F:\Git\30days-python\day1-introduction'
```

- Chạy lệnh `python.exe` với file Python ta muốn:

`PS F:\Git\30days-python\day1-introduction> python.exe .\result-day1.py`

Kết quả hiện thị:

<img src="https://imgur.com/Sc0KdW4.png">