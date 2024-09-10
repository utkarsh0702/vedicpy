from math import floor, log10

def isASquare(number: int) -> bool:
    num = number%10
    number=number//10
    if num==0:
        num = number%10
        number=number//10
        if num==0:
            num = number%10
            number=number//10
    if (num==2 or num==3 or num==7 or num==8):
        return False
    else:
        num1 = number
        sums = num
        while num1//10 != 0:
            sums += num1%10
            num1=num1//10
        sums+=num1
        # print(sums)
        # print(num)
        # print(number)
        if (sums==0 or sums==2 or sums==3 or sums==5 or sums==6 or sums==8):
            return False
        else:
            if num == 5:
                if number%10 == 2:
                    return True
                else:
                    return False
            
            elif num == 6:
                div = number%10
                if (div%2!=0):
                    return True
                else:
                    return False
            
            elif num == 1 or num == 4 or num == 9:
                div = number%10
                if (div%2==0):
                    return True
                else:
                    return False
            
            # elif num == 0 and sums==1:
            #     print("entered")
            #     try:
            #         print(log10(number*10))
            #         print(log10(number*10)%2)
            #         if log10(number*10)%2 != 0:
            #             print("passed")
            #             return True
            #         else:
            #             print("failed")
            #             return False
            #     except:
            #         return False
            
            else:
                return False
                
    
    
    


def perfect_sqrt_under_sqof100(a: int) -> int:
    if isASquare(a):
        c=0
        b=a%10
        # print(b)
        for i in range(100):
            if((i*10)**2 <= a ):
                if(a <= ((i+1)*10)**2):
                    c= i*10; break
        # print(c)
        
        d1= a-((i*10)**2)
        d2= (((i+1)*10)**2)-a
        
        if d2 == 0:
            return (i+1)*10
        
        # print(d1, d2)
        
        if(b==0): b=0

        elif(b==1): b= 1 if (d2>d1) else 9

        elif(b==4): b= 2 if (d2>d1) else 8

        elif(b==6): b= 4 if (d2>d1) else 6
        
        elif(b==9): b= 3 if (d2>d1) else 7
        
        elif(b==5): b= 5
        
        else:
            print("Error: Not a perfect square.")
            exit(0)
        # print(b)
        return (c+b)

    else:
        print('The number is not a perfect square....')
        exit(0)



print(perfect_sqrt_under_sqof100(1521))