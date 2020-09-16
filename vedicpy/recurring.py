def recuring_fractionto_decimal(divident: int, diviser: int) -> float:
    c, q, r = 0.0, 0, 0
    if(diviser%10 == 9):
        diviser= diviser
    elif(diviser%10 == 3):
        diviser= 3*diviser 
        divident= 3*divident
    elif(diviser%10 == 7):
        diviser= 7*diviser
        divident= 7*divident
    elif(diviser%10 == 1):
        diviser= 9*diviser
        divident= 9*divident
    else:
        print("Error: Not a recurring decimal.")
        exit(0)
    
    op= diviser/10 +1
    for i in range(0, 6):
        q= divident//op; r= divident%op
        divident= r*10 +q
        c= c+ q*(10**(-(i+1)))
    
    return round(c,6)