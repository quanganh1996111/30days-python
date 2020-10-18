empty_tuple=()
tuple_bros=('Tran Tuan Anh', 'Pham Thu Phuong', 'Nguyen Thi Thu Ha')
print(len(tuple_bros))
list_bros=list(tuple_bros)
parents=['Nguyen Thi Minh Dau', 'Tran Huy Hoang']
family_members=list_bros+parents
print(family_members)
fruits = ('banana', 'orange', 'mango', 'lemon')
vegatables = ('carrot', 'onion')
animal=('dog', 'cat', 'horse', 'rabbit')
food_stuff_tp=fruits+vegatables+animal
print(food_stuff_tp)
list_food_stuff_tp=list(food_stuff_tp)
print(list_food_stuff_tp)
middle_fst=list(food_stuff_tp[3:6])
print(middle_fst)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estoni' in nordic_countries)
print('Iceland' in nordic_countries)