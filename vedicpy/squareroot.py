from math import floor, log10

def squareroot_check(a: int) -> bool:
    a= int(a) ; b=a%10 ; x=a; a//=10
    if(b==2 or b==3 or b==7 or b==8):
        return False
    else:
        n= floor(log10(abs(x))) + 1 
        while(n!=1):
            sum=0
            while(x!=0):
                sum+=(x%10) ; x//=10
            x= sum
            n= floor(log10(abs(x))) + 1
            
        if(x==2 or x==3 or x==5 or x==6 or x==8 or x==9):
            return False
        else:
            if b==0:
                sum=0; i=0
                while(sum==0):
                    i+=1; sum= a%(10**i)
                if(i%2==0):
                    return True
                else:
                    return False
            
            elif(b==6):
                return True if((a%10)%2==1) else False
            else:
                return True if((a%10)%2==0) else False


def perfect_sqrt_under_sqof100(a: int) -> int:
    a= int(a)
    if(squareroot_check(a)==True):
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

    else:
        print('The number is not a perfect square.'); exit(0)