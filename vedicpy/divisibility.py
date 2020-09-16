def divisibility_under10(a: int, b: int):
    i=0
    if(b==2 or b==3 or b==4 or b==5 or b==6 or b==8 or b==9):
        if(b==2 and a%2==0): i=1
        
        elif(b==3):
            sum=0
            while(a!=0):
                sum+=a%10
                a//=10
            if(sum%3==0): i=1
        
        elif(b==4 and (a%100)%4==0): i=1

        elif(b==5 and (a%10==5 or a%10==0)): i=1
        elif(b==6 and a%2==0):
            sum=0
            while(a!=0):
                sum+=a%10
                a//=10
            if(sum%3==0): i=1
        
        elif(b==8 and (a%10000)%8==0): i=1
        
        elif(b==9):
            sum=0
            while(a!=0):
                sum+=a%10
                a//=10
            if(sum%9==0): i=1
    
    else:
        print("Error: The divisibility test is only applicable with 2,3,4,5,6,8 and 9.")
        exit(0)

    if(i==1):
        print("The number is divisible.")
    else:
        print("The number is not divisible.")
    