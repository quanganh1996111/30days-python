a='Thirty'
b='Days'
c='Of'
d='Python'
space = ' '
word= a + space + b + space + c + space + d
print(word)
code='Coding'
forr='For'
alll='All'
word2= code + space + forr + space + alll
print(word2)
company='Coding For All'
print(company)
print(len(company))
x=company.upper()
print(x)
y=company.lower()
print(y)
print(company.capitalize())
print(company.title())
print(company.swapcase())
first_word=company[0:1]
print(first_word)
sub_string='Coding'
print(word2.index(sub_string))
print(word2.replace('Coding', 'Python'))
print(word2.split())
word3="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(word3.split(', '))
print(word2.index('C'))
print(word2.index('F'))
word4='Coding For All People'
print(word4.rfind('l'))
sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
print(sentence.rindex('e'))
sub_sentence=sentence[31:54]
print(sub_sentence)
print(word2.startswith('Coding'))
print(word2.startswith('coding'))
word5='   Coding For All      '
print(word5.strip(' '))
python_lib=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result=' '.join(python_lib)
print(result)
print('I \nam \nenjoying \nthis \nchallenge.')
print('Name \tAge \tCountry')
radius = 10
area = 3.14 * radius ** 2
format_string='The area of a cricle with radius %d is %d merters square' %(radius, area)
print(format_string)
so1=8
so2=6
print(f'{so1} + {so2} = {so1 +so2}')
print(f'{so1} - {so2} = {so1 - so2}')
print(f'{so1} * {so2} = {so1 * so2}')
print(f'{so1} / {so2} = {so1 / so2:.2f}')
print(f'{so1} % {so2} = {so1 % so2}')
print(f'{so1} // {so2} = {so1 // so2}')
print(f'{so1} ** {so2} = {so1 ** so2}')