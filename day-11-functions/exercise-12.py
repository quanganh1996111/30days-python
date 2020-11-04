food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item(a):
    food_staff.pop(a)
    print(food_staff)
a = int(input('Thu tu muon xoa: '))
remove_item(a)