#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void divisibility_under10(int a, int b){
    int i=0;
    if(b==2 || b==3 || b==4|| b==5|| b==6|| b==8|| b==9){

        if(b==2 && a%2==0){ i=1; }
        if(b==3){
            int sum=0;
            while(a!=0){
                sum+=a%10;  a/=10;
            }
            if(sum%3==0){ i=1; }
        }
        if(b==4 && (a%100)%4==0){ i=1; }
        if(b==5 && (a%10==5 || a%10==0)){ i=1; }
        if(b==6 && a%2==0){
            int sum=0;
            while(a!=0){
                sum+=a%10;  a/=10;
            }
            if(sum%3==0){ i=1; }
        }
        if(b==8 && (a%10000)%8==0){ i=1; }
        if(b==9){
            int sum=0;
            while(a!=0){
                sum+=a%10;  a/=10;
            }
            if(sum%9==0){ i=1; }
        }
    }
    else{
        printf("Error: The divisibility test is only applicable with 2,3,4,5,6,8 and 9.\n");
        exit(0);
    }

    if(i==1){
        printf("The number is divisible.\n");
    }
    else{
        printf("The number is not divisible.\n");
    }
}