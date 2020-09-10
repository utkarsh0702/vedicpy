#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int cube_a_number(int a){
    int c,n= floor(log10(abs(a))) + 1, d1= a-pow(10,n), d2= a-pow(10,n-1);
    int d= abs(d1)>abs(d2) ? d2 : d1, b= abs(d1)>abs(d2) ? pow(10,n-1) : pow(10,n);
    int ne= d+ 2*d;
    if(d<0){
        for(int i=1;i<11;i++){
            if(abs(d*d*d)<(i*b)){
                c= (a+2*d)*pow(b,2) + (ne*d-i)*b + (i*b + d*d*d);
                break;
            }
        }
    }
    else{
        c= (a+2*d)*pow(b,2) + ne*d*b + d*d*d;
    }
    return c;
}

int cube_2digit_number(int a){
    int c,n= floor(log10(abs(a))) + 1;
    if(n==2 || n==1){
        int b=a%10;  a/=10;
        c= a*a*a*1000 + 3*a*a*b*100 + 3*a*b*b*10 + b*b*b;
    }
    else{
        printf("Error: Input should be a 2 digit number only.\n");
        exit(0);
    }
    return c;
}

int cuberoot_under_1000000(int a){
    int c=a%10;  a/=10;
    if(c==2){ c=8;}
    else if(c==3){ c=7;}
    else if(c==7){ c=3;}
    else if(c==8){ c=2;}
    a/=100;
    for(int i=1; i<11; i++){
        if(a<(i*i*i)){
            c+= (i-1)*10;
            break;
        }
    }
    return c;
}