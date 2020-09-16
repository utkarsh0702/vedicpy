from math import floor, log10

def multiply_by_9group(a: int) -> int:
    a= int(a)
    i=1; m=a; b= a%10; c=10-b
    a//=10 
    while(a!=0):
        b= a%10; a//=10
        c+= (9-b)*(10**i); i+=1
    
    m= (m-1)*(10**i)
    return (c+m)

def multiply_by11(a: int) -> int:
    a= int(a)
    c=a%10; b=b_prev=a%10; n = floor(log10(abs(a))) + 1
    a//=10
    for i in range(1, n+1):
        if(i== n):
            c+= b*(10**i)
        
        else:
            b=a%10; a//=10
            c+= (b+b_prev)*(10**i); b_prev=b
    
    return c

def multiply_by12(a: int) -> int:
    a= int(a)
    c= 2*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (2*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by13(a: int) -> int:
    a= int(a)
    c= 3*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (3*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by14(a: int) -> int:
    a= int(a)
    c= 4*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (4*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by15(a: int) -> int:
    a= int(a)
    c= 5*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (5*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by16(a: int) -> int:
    a= int(a)
    c= 6*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (6*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by17(a: int) -> int:
    a= int(a)
    c= 7*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (7*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by18(a: int) -> int:
    a= int(a)
    c= 8*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (8*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_by19(a: int) -> int:
    a= int(a)
    c= 9*(a%10); i=1; b_prev= a%10
    a//=10
    while(a!=0):
        b=a%10; a//=10
        c+= (9*b + b_prev)*(10**i); i+=1
        b_prev=b
    
    c+= b*(10**i)
    return c

def multiply_lastdigit_sumto10(a: int, b: int) -> int:
    a, b = int(a), int(b)
    if(((a%10) + (b%10)) ==10):
        if(a//10 == b//10 ):
            c= ((a%10) * (b%10))
            c+= (a//10)*(a//10 + 1)*100
        
        else:
            print("Error: Should have same previous digits.")
            exit(0)
    
    else:
        print("Error: Sum of last digit of both the number should be equal to 10.")
        exit(0)
    
    return c

def multiply_base_near_powerof10(a: int, b: int) -> int:
    a, b = int(a), int(b)
    i=1; m= floor(log10(abs(a))) + 1; n = floor(log10(abs(b))) + 1
    if(m==n):
        c= (a+b-(10**n))*(10**n)
        c+= (b-(10**n))*(a-(10**n))
    
    else:
        if(m<n):
            n=m
        
        c= (b-(10**n))*(a-(10**n))
        if((-1*c)>(10**n)):
            for i in range(2,10):
                if((-1*c) < i*(10**n)):
                    c+= i*(10**n); break
        
        else:
            c+= (10**n)
        
        c+= (a+b-(10**n)-i)*(10**n)
    
    return c

def multiply_equdigit_number(a: int, b: int) -> int:
    a, b = int(a), int(b)
    m= floor(log10(abs(a))) + 1; n = floor(log10(abs(b))) + 1
    if(m==n):
        if(m==2):
            x=a%10; y=b%10; a//=10; b//=10
            c= (a*b)*100 + (a*y + b*x)*10 + (x*y)
        
        elif(m==3):
            x=a%10; y=b%10; a//=10; b//=10
            u=a%10; v=b%10; a//=10; b//=10
            c= (a*b)*10000 + (u*b + v*a)*1000 + (x*b + a*y + u*v)*100 + (u*y + v*x)*10 + (x*y)
        
        elif(m==4):
            x=a%10; y=b%10; a//=10; b//=10
            u=a%10; v=b%10; a//=10; b//=10
            i=a%10; j=b%10; a//=10; b//=10
            c=(a*b)*1000000 + (a*j + b*i)*100000 + (a*v +b*u + i*j)*10000 + (a*y +b*x + i*v + j*u)*1000 + (i*y + j*x + u*v)*100 + (u*y + v*x)*10 + (x*y)
        
        else:
            print("Error: Only valid for 2, 3 and 4 digit numbers.")
            exit(0)
        
    else:
        print("Error: Number of digits need to be equal.")
        exit(0)
    
    return c
