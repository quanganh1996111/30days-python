# Strings - Dữ liệu kiểu chuỗi

Kiểu dữ liệu được viết dưới dạng văn bản là một chuỗi. Bất kỳ dữ liệu nào dưới dấu nháy đơn hoặc nháy kép đều là dữ liệu kiểu chuỗi. Có nhiều phương thức chuỗi khác nhau và các builtin-functions để xử lý các dữ liệu kiểu chuỗi. Hàm `len()` dùng để kiểm tra độ này của chuỗi.

## Creating a String

```
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```

Để tạo một đoạn chuỗi, ta sử dụng 3 dấu ngoặc đơn (''') hoặc 3 dấu ngoặc kép ("""). Ví dụ:

```
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# Another way of doing the same thing

multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

## String Concatenation

Chúng ta có thể các chuỗi với nhau bằng cách hợp nhất hoặc kết nối các chuỗi. Ví dụ:

```
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

## Escape Sequences in Strings - Trình tự thoát trong chuỗi

Một số lệnh để thoát các kí tự trong chuỗi:

- \n: Xuống dòng mới.

- \t: Giống việc sử dụng Tab trong soạn thảo (8 bước).

- \\\ : Dấu gạch chéo.

- \': Dấu ngoặc đơn (').

- \": Dấu ngoặc kép (").

Ví dụ:

```
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"')
```

Kết quả: 

```
I hope every one is enjoying the Python Challenge.
Are you ?
Days	Topics	Exercises
Day 1	5	    5
Day 2	6	    20
Day 3	5	    23
Day 4	1	    35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

## String formating - Định dạng chuỗi

### Old Style String Formating - Thay đổi định dạng chuỗi kiểu cũ (%)

Trong Python có nhiều cách để định dạnh lại chuỗi. Toán tử `%` được sử dụng để định dạng một tập hợp các biến kèm theo "tuple" (một danh sách kích thước cố định), chứa văn bản bình thường cùng với **argument specifiers**.

- %s : Định dạnh String.

- %d : Định dạng Số nguyên.

- %f : Định dạng Số thực.

- %.f : Định dạng Số thực với độ chính xác cố định.

Ví dụ:

```
# Strings only

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# Result

I am Asabeneh Yetayeh. I teach Python
```

```
# Strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area)

# Result

The area of circle with a radius 10 is 314.00.
```

```
python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)

# Result
The following are python libraries:['Django', 'Flask', 'Numpy', 'Pandas']
```

###  New Style String Formating (str.format)

Kiểu định dạng này được sử dụng trong Python Version 3

```
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

# Result
I am Asabeneh Yetayeh. I teach Python
```

```
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Result
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64
```

```
# Strings and numbers

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a cricle with a radius {} is {:.2f}.'.format(radius, area)
print(formated_string)

# Result
The area of a cricle with a radius 10 is 314.00.
```

### String Interpolation / f-Strings (Python 3.6+)

Trong Python 3.6+ có định dạng mới `f-strings`. String bắt đầu bằng `f` có thể dưa dữ liệu vào các vị trị tướng ứng.

```
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Result
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64
```

## Python Strings as Sequences of Characters

Chuỗi Python là chuỗi ký tự và chia sẻ các phương thức truy cập cơ bản của chúng với các chuỗi đối tượng có thứ tự Python khác - lists và tuples. Cách đơn giản nhất để trích xuất các ký tự đơn lẻ từ các chuỗi (và các thành viên riêng lẻ từ bất kỳ chuỗi nào) là giải nén chúng thành các biến tương ứng.

### Unpacking Characters

```
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

### Accessing Characters in Strings by Index

Trong lập trình được đếm từ số 0. Do đó, ký tự đầu tiên của chuỗi bắt đầu từ số 0 và ký tự cuối cùng của chuỗi là chiều dài của chuỗi trừ đi một.

<img src="https://imgur.com/qA7B9ac.png">

```
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

Nếu như muốn bắt đầu từ bên phải ta phải trừ -1.

```
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

### Slicing Python Strings - Cắt chuỗi ký tự trong Python

Trong Python ta có thể cắt chuỗi tới chuỗi con.

```
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(first_three) # Pyt
print(last_three) # hon

# Another way

last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

### Reversing a String - Đảo ngược chuỗi

Ta có thể đạo ngược Chuỗi trong Python một cách dễ dàng

```
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

## String Methods - Phương thức chuỗi

Có nhiều phương thức chuỗi cho phép chúng ta định dạng chuỗi.

- capitalize(): Viết hoa kí tự đầu trong chuỗi.

```
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```

- count(): trả về số lần xuất hiện của chuỗi con trong chuỗi, count(substring, start=.., end=..)

```
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2
```

- endswith(): Kiểm tra xem một chuỗi có kết thúc bằng một kết thúc được chỉ định hay không

```
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

- expandtabs(): Thay đổi Tab bằng khoảng trống, mặc định Tab là 8.

```
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

- find(): Trả về chỉ số thấp nhất của lần xuất hiện đầu tiên của một chuỗi con, nếu không tìm thấy thì trả về -1

```
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```

- rfind(): Trả về chỉ số cao nhất của lần xuất hiện đầu tiên của một chuỗi con, nếu không tìm thấy thì trả về -1

```
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```

- format(): Định dạng chuỗi sang một định dạng mà ta muốn. Ta có thể tham khảo [tại đây](https://www.programiz.com/python-programming/methods/string/format)

```
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)

# Result
I am Asabeneh Yetayeh. I am a teacher. I live in Finland.
```

```
radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result)

# Result
The area of a circle with radius 10 is 314.0
```

- index(): Trả về chỉ số thấp nhất của một chuỗi con, các đối số bổ sung cho biết chỉ số bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi - 1)

```
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string)) # 7

print(challenge.index(sub_string, 9))

# Result
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

- rindex(): Trả về chỉ số cao nhất của một chuỗi con, các đối số bổ sung cho biết chỉ số bắt đầu và kết thúc (mặc định là 0 và độ dài chuỗi - 1)

```
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string)) # 7

print(challenge.rindex(sub_string, 9))

# Result
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

- isalnum(): Kiểm tra ký tự chữ và số

```
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

- isalpha(): Kiểm tra xem tất cả các phần tử chuỗi có phải là các ký tự trong bảng chữ cái (a-z và A-Z) không

```
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

- isdecimal(): Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số thập phân (0-9) không

```
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, no space allowed
```

- isdigit(): Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số không (0-9 và một số ký tự unicode khác cho các số)

```
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

- isnumeric(): Kiểm tra xem tất cả các ký tự trong một chuỗi có phải là số hoặc có liên quan đến số hay không (giống như isdigit (), chỉ cần chấp nhận nhiều ký hiệu hơn, như ½)

```
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isidentifier(): Kiểm tra giá trị nhận dạng hợp lệ - có nghĩa là nó sẽ kiểm tra, nếu một chuỗi là tên biến hợp lệ

```
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

- islower(): Kiểm tra xem tất cả các ký tự bảng chữ cái trong chuỗi có phải là chữ thường không

```
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

- isupper(): Kiểm tra xem tất cả các ký tự bảng chữ cái trong chuỗi có phải là chữ hoa không

```
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

- join(): Trả về một chuỗi được nối

```
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)

# Result
HTML# CSS# JavaScript# React
```

- strip(): Loại bỏ tất cả các ký tự đã cho bắt đầu từ đầu và cuối chuỗi

```
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```

- replace(): Thay thế chuỗi con bằng một chuỗi đã cho

```
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```

- split(): Tách chuỗi, sử dụng chuỗi đã cho làm dấu phân tách

```
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

- title(): Trả về một chuỗi viết hoa tiêu đề

```
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

- swapcase(): Chuyển đổi tất cả các ký tự viết hoa thành chữ thường và tất cả các ký tự thường thành ký tự viết hoa

```
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```

- startswith(): Kiểm tra xem chuỗi có bắt đầu bằng chuỗi được chỉ định hay không

```
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```