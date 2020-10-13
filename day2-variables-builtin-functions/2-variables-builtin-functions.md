# Variables, Builtin Functions

## 1. Built in functions

Build-in functions là những hàm được cung cấp sẵn bởi ngôn ngữ Python, được hiểu là các function được đánh giá là "sử dụng nhiều" khi lập trình.

Một số functions kinh điển như: `sum`, `bin`, `max`, `min`, `len`, `...`

Khi sử dụng build-in function, chúng ta sẽ rút ngắn được code và trong một số trường hợp sẽ đảm bảo hiệu năng tính toán (với bài toán số "cực lớn" có thể gây tràn memory thì code tay sẽ cho độ phức tạp tính toán tốt hơn).

Chúng ta có thể tham khảo các Builtin Functions tại trang chủ của Python: https://docs.python.org/2/library/functions.html

<img src="https://imgur.com/O2vlZeE.png">

Tham khảo một số ví dụ về các builtin-functions [tại đây](https://codelearn.io/sharing/build-in-functions-trong-python)

## 2. Variables

**Biến (Variables)** được lưu trữ trong Memory của Máy tính, được sử dụng để lưu trữ thông tin. Một biến đề cập đến một địa chỉ bộ nhớ trong đó dữ liệu được lưu trữ. Không được phép sử dụng số ở đầu, ký tự đặc biệt, dấu gạch ngang khi đặt tên cho chúng. Một biến có thể có tên ngắn (như x, y, z), nhưng một tên mô tả chi tiết hơn (họ, tên, tuổi, quốc gia) được khuyến khích.

**Biến** giúp chúng ta lưu trữ các dữ liệu và cho phép chúng ta lấy các dữ liệu của chúng để tính toán được thuận tiện và chính xác hơn.

Quy tắc đặt tên biến trong Python:

- Tên biến phải bắt đầu bằng một chữ cái hoặc ký tự gạch dưới.

- Tên biến không thể bắt đầu bằng số.

- Tên biến chỉ có thể chứa các ký tự chữ-số và dấu gạch dưới (A-z, 0-9 và ký tự _).

- Tên biến có phân biệt chữ hoa chữ thường (tên, Firstname, FirstName và FIRSTNAME là các biến khác nhau).

Ví dụ:

- Các biến hợp lệ:

```
firstname
lastname
age
country
city
first_name
last_name
capital_city
_if # if we want to use reserved word as a variable
year_2019
year2019
current_year_2019
num1
num2
```

- Các biến không hợp lệ:

```
first-name
num-1
1num
```

### Khởi tạo một biến trong Python

Cú pháp:

`<tên biến>=<giá trị của biến>`

Kết quả:

<img src="https://imgur.com/TATLp74.png">

### Khởi tạo nhiều biến

Cú pháp:

`<tên biến thứ nhất>, <tên biến thứ hai>, ..,<tên tên biến thứ n> = <giá trị biến thứ nhất>, <giá trị biến thứ hai>, .., <giá trị biến thứ n>`

Kết quả:

<img src="https://imgur.com/fYTkZpU.png">

## Data Types

Trong Python có một kiểu dữ liệu, để kiểm tra kiểu dữ liệu ta sử dụng builtin-function `type`. Kiểu dữ liệu đã được giới thiệu trong [day1-introduction](https://github.com/quanganh1996111/30days-python/blob/master/day1-introduction/2-basic-python.md)

Chuyển một kiểu dữ liệu sang một kiểu dữ liệu khác. Ta sử dụng `int(), float(), str(), list`. Khi chúng ta thực hiện các phép toán số học, đầu tiên các số chuỗi phải được chuyển đổi thành int hoặc float, nếu không nó sẽ trả về lỗi. Nếu chúng ta nối một giá trị kiểu `number` với một giá trị `string`, ta phải chuyển giá trị từ `number` sang `string` trước khi nối.

Ví dụ:

```
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)
print(first_name)                    # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
```

### Numbers Data types

Các kiểu dữ liệu Number trong Python:

- Integers: Số nguyên (nguyên âm, 0 và nguyên dương). Ví dụ: -3, -2, -2, 0, 1, 2, 3,...

- Floating Point Numbers (Số thập phân). Ví dụ: 3.24, -3.13, -1.0, 0.0, 1.0, 2.5,...

- Complex Numbers (Số phức). Ví dụ: 1 + j, 2 + 4j, 1 - 4j,... 