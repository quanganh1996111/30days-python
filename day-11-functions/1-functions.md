# Functions in Python

Cho đến nay chúng ta đã thấy nhiều hàm python được tích hợp sẵn. Trong phần này,chúng ta sẽ tập trung vào các chức năng tùy chỉnh. Hàm là gì? Trước khi bắt đầu tạo hàm, chúng ta hãy tìm hiểu hàm là gì và tại sao chúng ta cần chúng?

## Defining a Function

Hàm là một khối mã hoặc câu lệnh lập trình có thể sử dụng lại được thiết kế để thực hiện một tác vụ nhất định. Để định nghĩa một hàm, Python cung cấp từ khóa `def`. Sau đây là cú pháp để xác định một hàm. Khối mã chức năng chỉ được thực thi khi chúng ta gọi nó.

## Declaring and Calling a Function

Khi chúng ta tạo một hàm, chúng ta gọi nó là khai báo một hàm. Khi chúng ta bắt đầu sử dụng nó, chúng ta gọi nó là gọi hoặc gọi một hàm. Hàm có thể được khai báo có hoặc không có tham số.

```
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a function
function_name()
```

## Function without Parameters

Hàm có thể được khai báo mà không có tham số.

```
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

## Function Returning a Value - Part 1

Hàm cũng có thể trả về giá trị, nếu một hàm không trả về giá trị nào thì giá trị của hàm là `None`. Cho phép viết lại các hàm trên bằng cách sử dụng `return`. Từ bây giờ, chúng ta nhận được một giá trị khi gọi hàm, thay vì in nó.

```
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

## Function with Parameters

Trong một hàm, chúng ta có thể chuyển các kiểu dữ liệu khác nhau (number, string, boolean, list, tuple, dictionary or set) dưới dạng tham số.

- Single Parameter: Nếu hàm của chúng ta nhận một tham số, chúng ta nên gọi hàm của chúng ta bằng một đối số

```
 # syntax
  # Declaring a function
  def function_name(parameter):
    codes
    codes
  # Calling function
  function_name(parameter)
```

Ví dụ:

```
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    print(total)
sum_of_numbers(10) # 55
sum_of_numbers(100) # 5050
```

- Two Parameter: Một hàm có thể có hoặc không có tham số hoặc các tham số. Một hàm có thể có hai hoặc nhiều tham số. Nếu hàm của chúng ta nhận tham số, chúng ta nên gọi nó với các đối số. Hãy kiểm tra một hàm với hai tham số.

```
 # syntax
  # Declaring a function
  def function_name(para1, para2):
    codes
    codes
  # Calling function
  function_name(arg1, arg2)
```

ví dụ:

```
def generate_full_name (first_name, last_name):
    space = ' '
      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;

print('Age: ', calculate_age(2019, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

## Passing Arguments with Key and Value

Nếu chúng ta truyền các đối số có `key` và `value`, thứ tự của các đối số không quan trọng.

```
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
function_name(para1='John', para2='Doe') # the order of arguments does not matter here
```

Ví dụ:

```
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname='Asabeneh', lastname='Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
add_two_numbers(num2=3, num1=2) # Order does not matter
```

## Function Returning a Value - Part 2

Nếu chúng ta không trả về giá trị bằng một hàm, thì hàm của chúng ta đang trả về `None` mặc định. Để trả về một giá trị với một hàm, chúng ta sử dụng từ khóa `return` theo sau là biến chúng ta đang trả về. Chúng ta có thể trả về bất kỳ kiểu dữ liệu nào từ một hàm.

- Trả về String:

```
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- Trả về Number:

```
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(2019, 1819))
```

- Trả về boolean:

```
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return stops further execution of the function, similar to break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- Trả về List:

```
def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

## Function with Default Parameters

Đôi khi chúng ta chuyển các giá trị mặc định cho các tham số, khi chúng ta gọi hàm. Nếu chúng ta không truyền các đối số khi gọi hàm, các giá trị mặc định của chúng sẽ được sử dụng.

```
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

Ví dụ:

```
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2019):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1819))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon
```

## Arbitrary Number of Arguments

Nếu chúng ta không biết số lượng đối số mà chúng ta truyền vào hàm của mình, chúng ta có thể tạo một hàm có thể nhận số lượng đối số tùy ý bằng cách thêm `*` vào trước tên tham số.

```
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

Ví dụ:

```
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5))
```

## Default and Arbitrary Number of Parameters in Functions

Sử dụng tham số mặc định và tùy ý trong Hàm.

```
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

## Function as a Parameter of Another Function

Chức năng như một tham số của một hàm khác.

```
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3))
```