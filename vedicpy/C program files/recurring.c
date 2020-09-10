#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void recuring_fractionto_decimal(int divident, int diviser){
    float c=0;  int q=0,r=0;
    if(diviser%10 == 9){ diviser= diviser;}
    else if(diviser%10 == 3){ diviser= 3*diviser; divident= 3*divident;}
    else if(diviser%10 == 7){ diviser= 7*diviser; divident= 7*divident;}
    else if(diviser%10 == 1){ diviser= 9*diviser; divident= 9*divident;}
    else{
        printf("Not a recurring decimal.\n");
        exit(0);
    }
    int op= diviser/10 +1;
    for(int i=0;i<6;i++){
        q= divident/op; r= divident%op;
        divident= r*10 +q;
        c= c+ q*pow(10, -(i+1));
    }
    printf("%f\n",c);
}