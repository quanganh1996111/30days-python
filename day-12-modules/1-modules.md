# Modules in Python

## What is a Module

Một Module là một tệp chứa một bộ mã hoặc một bộ chức năng có thể được đưa vào ứng dụng. Một mô-đun có thể là một tệp chứa một biến duy nhất hoặc một hàm, một cơ sở mã lớn.

## Creating a Module

Để tạo một Module, chúng ta viết mã của chúng tôi trong một tập lệnh python và chúng tôi lưu nó dưới dạng tệp .py. Tạo một tệp có tên mymodule.py bên trong thư mục dự án của bạn. Hãy viết một số mã trong tệp này.

```
# mymodule.py file
def generate_full_name(firstname, lastname):
    space = ' '
    fullname = firstname + space + lastname
    return fullname
```

Tạo file main.py trong Project của chúng ta và thêm các files module.py.

## Importing a Module

Để thêm file Module ta sử dụng `import` và tên file Module.

```
# main.py file
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))
```

## Import Functions from a Module

Chúng ta có thể có nhiều hàm trong một tệp và chúng ta có thể nhập tất cả các hàm theo cách khác nhau.

```
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetay'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```

## Import Functions from a Module and Renaming

Trong quá trình nhập, chúng tôi có thể đổi tên của Module.

```
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1,9))
mass = 100;
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Import Built-in Modules

Giống như các ngôn ngữ lập trình khác, chúng ta cũng có thể nhập các mô-đun bằng cách nhập tệp / hàm bằng từ khóa `import`. Hãy nhập Module chung mà chúng ta sẽ sử dụng hầu hết thời gian. Một số Module được tích hợp sẵn phổ biến như: `math, datetime, os,sys, random, statistics, collections, json,re`.

## OS Module

Sử dụng `os` Module có thể tự động thực hiện nhiều tác vụ của hệ điều hành. Module `os` trong Python cung cấp các chức năng để tạo, thay đổi thư mục làm việc hiện tại và xóa thư mục, tìm nạp nội dung của nó, thay đổi và xác định thư mục hiện tại.

```
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

## Sys Module

Module `sys` cung cấp các hàm và biến được sử dụng để thao tác các phần khác nhau của môi trường thời gian chạy Python. Hàm `sys.argv` trả về danh sách các đối số dòng lệnh được chuyển đến tập lệnh Python. Giá trị `index 0` trong List luôn luôn là cái tên xuất hiện trong tập lệnh, `index 1` là đối số được truyền từ dòng lệnh.

Ví dụ file `script.py`:

```
import sys
#print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

Kiểm tra file Script hoạt động như thế nào khi chúng ta viết lệnh:

`python script.py Asabeneh 30DaysOfPython`

Kết quả:

`Welcome Asabeneh. Enjoy  30DayOfPython challenge! `

Một số Lệnh `sys` hữu ích:

```
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

## Statistics Module

Module thống kê cung cấp các chức năng để thống kê toán học của dữ liệu số. Các hàm thống kê phổ biến được định nghĩa trong Module: `mean, median, mode, stdev, ...`

```
from statistics import * # importing all the statistics modules
ages = [20,20,24,24,25,22,26,20,23,22,26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

## Math Module

Module chứa nhiều phép toán và hằng số.

```
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithim with 10 as base
```

Bây giờ, Chúng ta đã nhập Module toán học có chứa rất nhiều hàm có thể giúp chúng tôi thực hiện các phép tính toán học. Để kiểm tra các chức năng mà mô-đun có, chúng ta có thể sử dụng `help(math)`, hoặc `dir(math)`. Điều này sẽ hiển thị các chức năng có sẵn trong Module. Nếu chúng tôi chỉ muốn nhập một chức năng cụ thể từ mô-đun, chúng tôi nhập nó như sau:

```
from math import pi
print(pi)
```

Chúng ta có thể thêm nhiều hàm cùng một lúc:

```
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
```

Chúng ta có thể thêm tất cả các hàm trong Math Module bằng cách sử dụng `*`.

```
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
```

Khi ta thêm một hàm chúng ta có thể đổi tên cho hàm đó.

```
from math import pi as  PI
print(PI) # 3.141592653589793
```

## String Module

Một Module hữu ích cho nhiều mục đích. Dưới đây là một ví dụ về chuỗi mà chúng tôi có thể lấy từ nó.

```
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

## Random Module

Bây giờ bạn đã quen với việc nhập các mô-đun. Hãy thực hiện thêm một lần nhập nữa để làm quen với nó. Ta thêm `random` Module cho chúng ta một số ngẫu nhiên từ 0 đến 0,9999 .... Module `random` có rất nhiều chức năng nhưng trong phần này chúng tôi sẽ chỉ sử dụng `random` và `randint`.

```
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between 5 and 20
```