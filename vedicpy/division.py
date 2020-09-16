def division_by9(a: int):
    summ = i = q = 0
    arr=[]
    while(a!=0):
        b, a = a%10, a//10
        summ+=b
        arr.append(b)
    
    if(summ>=9):
        for j in range(2,8):
            if(summ<(9*j)):
                i= j-1
                r= summ- (9*(j-1))
                break
            
    else:
        r= summ
    
    b=0
    for j in range(len(arr)-1, 0, -1):
        b+= arr[j]
        q+= b*(10**(j-1))
    q+=i
    print("The quotent is: ",q)
    print("The reminder is: ",r)