#include<stdio.h>
#include<math.h>

int compliment_to_power_of10(int a){
    int i=1, b= a%10, c=10-b; 
    a/=10; 
    while(a!=0){
        b= a%10; a/=10;
        c+= (9-b)*pow(10,i); i++;
    }
    return c;
}