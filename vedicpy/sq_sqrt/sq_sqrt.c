#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int square_ending5(int a){
    int c;
    if(a%10 == 5){
        c= (a/10)*((a/10)+1)*100 +25;
    }
    else{
        printf("Error: The lat digit of the nu,ber should be 5.\n");
    } 
    return c;
}

int square_near_powerof10(int a){
    int c, n= floor(log10(abs(a))) + 1, d1= a-pow(10,n), d2= a-pow(10,n-1);
    c= abs(d1)>abs(d2) ? d2 : d1;
    n= abs(d1)>abs(d2) ? n-1 : n;
    c= (a+c)*pow(10,n) + c*c;
    return c;
}


int square_under100(int a){
    int c,n= floor(log10(abs(a))) + 1;
    if(n==1 || n==2){
        int b= a%10;  a/=10;
        c= a*a*100+ 2*a*b*10 +b*b;
    }
    else{
        printf("Error: Number should be less than 100.\n");  exit(0);
    }
    return c;
}

int square_from100_to1000(int a){
    int result,n= floor(log10(abs(a))) + 1;
    if(n==3){
        int b,c= a%10;  a/=10; b= a%10; a/=10;
        result= a*a*10000+ 2*a*b*1000 + (b*b + 2*a*c)*100+ 2*b*c*10+ c*c;
    }
    else{
        printf("Error: Number should be between 100 and 1000.\n");  exit(0);
    }
    return result;
}

int perfect_sqrt_under_sqof100(int a){
    int c=0,i,b= a%10;
    for(i=0;i<100;i++){
        if(pow(i*10, 2)<= a ){
            if(a <= pow((i+1)*10, 2)){
                c= i*10;
            break;
            }
        }
    }
    int d1= a- pow(i*10, 2), d2= pow((i+1)*10, 2)- a;
    if(b==0){
        b=0;}
    else if(b==1){
        b= (d2>d1)? 1: 9;}
    else if(b==4){
        b= (d2>d1)? 2: 8;}
    else if(b==6){
        b= (d2>d1)? 4: 6;}
    else if(b==9){
        b= (d2>d1)? 3: 7;}
    else if(b==5){
        b= 5;}
    else{
        printf("Error: Not a perfect square.\n");
        exit(0);}
    
    return (c+b);
}