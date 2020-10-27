# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies2={'Nhan Hoa', 'Tecapro', 'Viet Sunshine'}
it_companies.update(it_companies2)
print(it_companies)
C=A.union(B)
D=A.update(B)
E=B.update(A)
print(C)
print(A.issubset(B))
print(A.isdisjoint(B))
print(D)
print(E)
print(A.symmetric_difference(B))
del A
del B
age_set=set(age)
print(len(age))
print(len(age_set))
sentence={'I', 'am', 'a', 'teacher', 'and', 'I', 'love', 'to', 'inspire', 'and', 'teach', 'people'}
print(len(sentence))