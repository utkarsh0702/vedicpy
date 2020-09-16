def compliment_to_power_of10(a: int) -> int:
    i, b = 1, a%10
    c, a = 10-b, a//10
    while a!=0:
        b, a= a%10, a//10
        c+= (9-b)*pow(10,i)
        i+=1
    return c
