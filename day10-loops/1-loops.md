# Loops in Python

Trong các Ngôn ngữ lập trình, chúng ta cũng sẽ làm rất nhiều công việc lặp đi lặp lại. Để xử lý những công việc đó, chúng ta tạo ra các vòng lặp `loops`. Trong Python, chúng ta có 2 loại vòng lặp:

- while loop.

- for loop.

## While Loop

Chúng ta sử dụng `while` để tạo vào lặp while. Nó được sử dụng để thực hiện lặp đi lặp lại một khối câu lệnh cho đến khi thỏa mãn một điều kiện nhất định. Khi điều kiện trở thành sai, các dòng mã sau vòng lặp sẽ được tiếp tục thực hiện.

```
# syntax
while condition:
    code goes here
```

Ví dụ:

```
count = 0
while count < 5:
    print(count)
    count = count + 1
```

Điều kiện trở thành sai khi số đếm là 5. Đó là khi vòng lặp dừng lại. Nếu chúng ta muốn chạy khối mã khi điều kiện không còn đúng nữa, chúng ta có thể sử dụng phương thức `else`.

```
  # syntax
while condition:
    code goes here
else:
    code goes here
```

Ví dụ:

```
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

Vòng lặp trên sẽ `false` khi đếm đến 5 và vòng lặp dừng lại, và bắt đầu thực thi lệnh `else`. Kết quả là 5 sẽ được in ra.

## Break and Continue - Part 1

- Break: Chúng ta sử dụng Break khi chúng ta muốn thoát hoặc dừng vòng lặp.

```
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

Ví dụ:

```
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

Vòng lặp trên chỉ in ra số `0, 1, 2` nhưng khi đến `3` thì dừng.

- Continue: Với câu lệnh `continue`, chúng ta có thể dừng lần lặp hiện tại và tiếp tục với phần tiếp theo:

```
# syntax
while condition:
    code goes here
    if another_condition:
        continue
```

Ví dụ:

```
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
```

Vòng lặp while ở trên chỉ in 0, 1, 2 và 4 (bỏ qua 3).

## For Loop

Từ khóa `for` được sử dụng để tạo vòng lặp `for`, tương tự với các ngôn ngữ lập trình khác nhưng có một số khác biệt về cú pháp.  Vòng lặp được sử dụng để lặp qua một chuỗi (List, Tuple, Dictionary, Set hoặc là String).

- Vòng lặp `for` với List:

```
# syntax
for iterator in lst:
    code goes here
```

Ví dụ:

```
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
```

- Vòng lặp `for` với String:

```
# syntax
for iterator in string:
    code goes here
```

Ví dụ:

```
language = 'Python'
for letter in language:
    print(letter)
```

- Vòng lặp `for` với tuple:

```
# syntax
for iterator in tpl:
    code goes here
```

Ví dụ:

```
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
```

- Vòng lặp `for` với Dictionary cho chúng ta `key` trong Dictionary:

```
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

- Vòng lặp với Set:

```
# syntax
for iterator in st:
    code goes here
```

Ví dụ:

```
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

## Break and Continue - Part 2

- Short Reminder: Sử dụng `break` khi chúng ta muốn dừng vòng lặp trước khi nó hoàn thành.

```
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

Ví dụ: Vòng lặp dừng lại khi đếm đến 3.

```
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

- Continue: Chúng ta sử dụng `continue` khi chúng ta muốn bỏ qua một số bước trong quá trình lặp lại của vòng lặp.

```
# syntax
for iterator in sequence:
    code goes here
    if condition:
        continue
```

Ví dụ: Nếu như số bằng 3, bước sau điều kiện (nhưng bên trong vòng lặp) bị bỏ qua và việc thực hiện vòng lặp tiếp tục nếu còn lại bất kỳ lần lặp nào.

```
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
```

## The Range Function

Lệnh `range()` được sử dụng để lặp qua một bộ mã một số lần nhất định. Lệnh `range(start,end,step)` tương ứng với 3 phần: bắt đầu, kết thúc và tăng dần. Theo mặc định, nó bắt đầu từ 0 và gia số là 1. Chuỗi phạm vi cần ít nhất 1 đối số (kết thúc). Tạo chuỗi sử dụng `range`.

```
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```
# syntax
for iterator in range(start, end, increment):
```

Ví dụ:

```
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

## Nested For Loop

Chúng ta có thể lồng vòng lặp trong vòng lặp khác.

```
# syntax
for x in y:
    for t in s:
        print(t)
```

Ví dụ:

```
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

## For Else

Nếu chúng ta muốn thực thi một số thông báo khi vòng lặp kết thúc, chúng ta sử dụng `else`.

```
# syntax
for iterator in range(start, end, increment):
    do something
else:
    print('The loop ended')
```

Ví dụ:

```
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```

## Pass

Trong python khi câu lệnh được yêu cầu (sau dấu chấm phẩy), nhưng chúng ta không muốn thực thi bất kỳ mã nào ở đó, chúng ta có thể dùng `pass` để tránh lỗi. Ngoài ra, chúng ta có thể sử dụng nó như một trình giữ chỗ, cho các câu lệnh trong tương lai.

Ví dụ:

```
for number in range(6):
    pass
```