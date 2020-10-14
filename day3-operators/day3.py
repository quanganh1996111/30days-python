# Day 3 Exercies

# Level 1
age=(int(input('Tuoi cua ban la: ')))
height=(float(input('Chieu cao cua ban la: ')))
complexnumber=1+1j

# Level 2
base=(float(input('Canh huyen tam giac la: ')))
high=(float(input('Chieu cao cua tam giac la:')))
area=0.5*base*high
print('Dien tich hinh tam giac la: ',area)

# Level 3
side_a=(float(input('Canh a: ')))
side_b=(float(input('Canh b: ')))
side_c=(float(input('Canh c: ')))
perimeter=side_a+side_b+side_c
print('Chu vi hinh tam giac la: ',perimeter)

# Level 4
length=(float(input('Chieu dai hinh chu nhat la:')))
width=(float(input('Chieu rong hinh chu nhat la:')))
area_rec=length*width
peri_rec=2*(length+width)
print('Dien tich hinh chu nhat la: ',area_rec)
print('Chu vi hinh chu nhat la:', peri_rec)

# Level 5
pi=3.14
radius=(float(input('Ban kinh hinh tron la: ')))
area_circle=pi*radius*radius
peri_circle=2*pi*radius
print('Dien tich hinh tron: ',area_circle)
print('Chu vi hinh tron: ',peri_circle)