# Conditionals

Theo mặc định, các câu lệnh trong tập lệnh của Python được thực thi tuần tự từ trên xuống dưới. Nếu logic xử lý yêu cầu như vậy, luồng thực thi tuần tự có thể được thay đổi theo hai cách:

- **Conditional Execution** (Thực thi có điều kiện): Một khối gồm một hoặc nhiều câu lệnh được thực hiện nếu một biểu thức nhất định là đúng.

- **Repetitive execution** (Thực thi lặp lại): Một khối gồm một hoặc nhiều câu lệnh sẽ được thực hiện lặp đi lặp lại miễn là một biểu thức nào đó là đúng. Trong phần này, chúng ta sẽ đề cập đến các câu lệnh `if, else, elif`.

## If Condition

Trong Python và các ngôn ngữ lập trình khác, từ khóa nếu chúng ta sử dụng để kiểm tra xem một điều kiện có đúng không và để thực thi mã khối. Hãy nhớ dấu thụt vào sau dấu hai chấm.

```
# syntax
if condition:
    this part of code runs for truthy conditions
```

Ví dụ:

```
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

Trong ví dụ trên, 3 lớn hơn 0. Điều kiện là đúng và mã khối đã được thực thi. Tuy nhiên, nếu điều kiện sai, chúng ta không thấy kết quả. Để xem kết quả của điều kiện giả, chúng ta nên có một khối khác, đó là `else`.

## If Else

Nếu điều kiện là đúng, khối đầu tiên sẽ được thực thi, nếu không, điều kiện khác sẽ chạy.

```
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

Ví dụ:

```
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

Điều kiên chứng tỏ `else`, thì khối `else` sẽ được thực thi. Nếu như trường hợp xảy ra nhiều hơn hai ? Chúng ta có thể sử dụng `_elif_`.

## If elif Else

Trong cuộc sống hàng ngày, chúng ta đưa ra quyết định hàng ngày. Chúng ta đưa ra quyết định không phải bằng cách kiểm tra một hoặc hai điều kiện mà là nhiều điều kiện. Tương tự như cuộc sống, lập trình cũng có đầy đủ các điều kiện. Chúng ta sử dụng `elif` khi chúng ta sử dụng nhiều điều kiện.

```
# syntax
if condition:
    code
elif condition:
    code
else:
    code
```

Ví dụ:

```
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

## Short Hand

```
# syntax
code if condition else code
```

Ví dụ:

```
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
```

## Nested Conditions

```
if condition:
    code
    if condition:
    code
```

Ví dụ:

```
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

Chúng ta có thể tránh việc lồng các điều kiện bằng các sử dụng toán tử logic `and`.

## If Condition and Logical Operators

```
# syntax
if condition and condition:
    code
```

Ví dụ:

```
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 != = 0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

## If and Or Logical Operators

```
# syntax
if condition or condition:
    code
```

Ví dụ:

```
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```