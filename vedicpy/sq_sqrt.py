from math import floor, log10

def square_ending5(a: int) -> int:
    a= int(a)
    if(a%10 == 5):
        c= (a//10)*((a//10)+1)*100 +25
    else:
        print("Error: The last digit of the number should be 5.")
        exit(0)
    
    return c

def square_near_powerof10(a: int) -> int:
    a= int(a)
    n= floor(log10(abs(a))) + 1
    d1= a-(10**n); d2= a-(10**(n-1))
    c= d2 if abs(d1)>abs(d2) else d1
    n= n-1 if abs(d1)>abs(d2) else n
    c= (a+c)*(10**n) + c*c
    return c

def square_under100(a: int) -> int:
    a= int(a)
    n= floor(log10(abs(a))) + 1
    if(n==1 or n==2):
        b= a%10;  a//=10
        c= a*a*100+ 2*a*b*10 + b*b
    
    else:
        print("Error: Number should be less than 100.");  exit(0)
    
    return c

def square_from100_to1000(a: int) -> int:
    a= int(a)
    n= floor(log10(abs(a))) + 1
    if(n==3):
        c= a%10;  a//=10; b= a%10; a//=10
        result= a*a*10000+ 2*a*b*1000 + (b*b + 2*a*c)*100+ 2*b*c*10+ c*c
    
    else:
        print("Error: Number should be between 100 and 1000.");  exit(0)
    
    return result

def perfect_sqrt_under_sqof100(a: int) -> int:
    a= int(a)
    c=0; b= a%10
    for i in range(100):
        if((i*10)**2 <= a ):
            if(a <= ((i+1)*10)**2):
                c= i*10; break
    
    d1= a- ((i*10)**2); d2= (((i+1)*10)**2)- a
    if(b==0): b=0

    elif(b==1): b= 1 if (d2>d1) else 9

    elif(b==4): b= 2 if (d2>d1) else 8

    elif(b==6): b= 4 if (d2>d1) else 6
    
    elif(b==9): b= 3 if (d2>d1) else 7
    
    elif(b==5): b= 5
    
    else:
        print("Error: Not a perfect square."); exit(0)
    
    return (c+b)