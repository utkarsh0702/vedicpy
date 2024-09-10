def divisibility_under10(a: int, b: int) -> bool:
    flag = False
    
    if( b>=2 and b<=9):
        if(b==2 and a%2==0): 
            flag = True
        
        elif(b==3):
            sum=0
            while(a!=0):
                sum+=a%10
                a//=10
            if(sum%3==0):
                flag = True
        
        elif(b==4 and (a%100)%4==0):
            flag = True

        elif(b==5 and (a%10==5 or a%10==0)):
            flag = True
        
        elif(b==6 and a%2==0):
            sum=0
            while(a!=0):
                sum+=a%10
                a//=10
            if(sum%3==0):
                flag = True
        
        elif(b==7):
            unit, num = a%10, a//10
            if (num - 2*unit)%7 == 0:
                flag = True
        
        elif(b==8 and (a%10000)%8==0):
            flag = True
        
        elif(b==9):
            sum=0
            while(a!=0):
                sum+=a%10
                a//=10
            if(sum%9==0):
                flag = True
    
    else:
        print("Error: The divisibility test is only implemented for 2 to 9.")
        exit(0)
    
    return flag