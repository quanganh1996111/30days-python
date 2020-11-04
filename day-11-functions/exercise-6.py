def slope(x1, y1, x2, y2): 
    return (float)(y2-y1)/(x2-x1)  
     
x1 = int(input('x1: '))
y1 = int(input('y1: ')) 
x2 = int(input('x2: ')) 
y2 = int(input('y2: '))
print ("Slope is :", slope(x1, y1, x2, y2))
