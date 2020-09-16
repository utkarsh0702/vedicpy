from math import floor, log10

def cube_a_number(a: int) -> int:
    n = floor(log10(abs(a))) + 1 
    d1, d2= a-(10**n), a-(10**(n-1))
    d= d2 if abs(d1)>abs(d2) else d1
    b= 10**(n-1) if abs(d1)>abs(d2) else 10**n
    ne= d+ 2*d
    if(d<0):
        for i in range(1,11):
            if(abs(d*d*d)<(i*b)):
                c= (a+2*d)*(b**2) + (ne*d-i)*b + (i*b + d*d*d)
                break
    else:
        c= (a+2*d)*(b**2) + ne*d*b + d*d*d
    
    return c

def cube_2digit_number(a: int) -> int:
    a= int(a)
    n= floor(log10(abs(a))) + 1
    if(n==2 or n==1):
        b, a = a%10, a//10
        c= (a**3)*1000 + 3*(a**2)*b*100 + 3*a*(b**2)*10 + b**3
    
    else:
        print("Error: Input should be a 2 digit number only.")
        exit(0)

    return c

def cuberoot_under_1000000(a: int) -> int:
    a= int(a)
    c, a = a%10, a//10
    if(c==2): c=8
    elif(c==3): c=7
    elif(c==7): c=3
    elif(c==8): c=2
    a//=100
    for i in range(1,11):
        if(a<(i**3)):
            c+= (i-1)*10
            break
    
    return c