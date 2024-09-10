from math import floor, log10

def isACube(a: int) -> bool:
    n= floor(log10(abs(a))) + 1 
    while(n!=1):
        sum=0
        while(a!=0):
            sum+=(a%10) ; a//=10
        a= sum
        n= floor(log10(abs(a))) + 1
        
    if(a==1 or a==8 or a==9 or a==0):
        return True
    else:
        return False

def cuberoot_under_a_million(a: int) -> int:
    if isACube(a):
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
    else:
        print('The number is not a perfect cube.'); exit(0)



def cuberoot_under_thousand(num: int) -> float:
    cubeRootList = [1,8,27,64,125,216,343,512,729,1000]
    nearest_num = min(cubeRootList, key=lambda x:abs(x-num))
    diff = num - nearest_num
    output = cubeRootList.index(nearest_num)+1
    if diff != 0:
        output = round(float(output) + diff/(3*output*output), 4)
    return output