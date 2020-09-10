#include<stdio.h>
#include<math.h>

int division_by9(int a){
    int sum=0, arr[10],i=0,j,b,q=0,r;
    while(a!=0){
        b=a%10; a/=10;
        sum+=b; arr[i]=b; i++;
    }
    if(sum>9){
        for(j=2; j<8; j++){
            if(sum<(9*j)){
                r= sum- (9*(j-1)); break;
            }
        }
    }
    else{
        r= sum;
        }
    b=0;
    for(j=i-1;j>0;j--){
        b+= arr[j];
        q+= b*pow(10,j-1);
    }
    printf("The quotent is: %d\n",q);
    printf("The reminder is: %d\n",r);
}