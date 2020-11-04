def findseason (M) : 
    list1 = [[1 , 2 , 3], [4 , 5 , 6],  
             [7 , 8 , 9], [10 , 11 , 12]] 
    if M in list1[0] : 
        print ( "WINTER" ) 
    elif M in list1[1] : 
        print ( "SPRING" ) 
    elif M in list1[2] : 
        print ( "SUMMER" ) 
    elif M in list1[3] : 
        print ( "AUTUMN" ) 
    else : 
        print ( "Do khong phai thang trong mot nam" ) 

M = int(input('Thang: '))
print("For Month number:", M); 
findseason ( M ) 