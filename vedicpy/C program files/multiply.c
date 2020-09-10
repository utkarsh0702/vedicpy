#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int multiply_by11(int a){
    int c=a%10,i,b,b_prev=a%10, n = floor(log10(abs(a))) + 1, m= (a-1)*pow(10,n);
    a/=10;
    for(i=1;i<n+1; i++){
        if(i== n){
            c+= b*pow(10,i);
        }
        else{
            b=a%10;
            a/=10;
            c+= (b+b_prev)*pow(10,i);
            b_prev=b;
        }
    }
    return c;
}

int multiply_by_9group(int a){
    int i=1,m=a, b= a%10, c=10-b;
    a/=10; 
    while(a!=0){
        b= a%10; a/=10;
        c+= (9-b)*pow(10,i); i++;
    }
    m= (m-1)*pow(10,i);
    return (c+m);
}

int multiply_by12(int a){
    int c= 2*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (2*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by13(int a){
    int c= 3*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (3*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by14(int a){
    int c= 4*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (4*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by15(int a){
    int c= 5*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (5*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by16(int a){
    int c= 6*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (6*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by17(int a){
    int c= 7*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (7*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by18(int a){
    int c= 8*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (8*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_by19(int a){
    int c= 9*(a%10),i=1, b_prev= a%10, b;
    a/=10;
    while(a!=0){
        b=a%10; a/=10;
        c+= (9*b + b_prev)*pow(10,i);  i++;
        b_prev=b; 
    }
    c+= b*pow(10,i);
    return c;
}

int multiply_sumto10(int a, int b){
    int c;
    if(((a%10) + (b%10)) ==10){
        if(a/10 == b/10 ){
            c= ((a%10) * (b%10));
            c+= (a/10)*(a/10 + 1)*100;
        }
        else{
            printf("Error: Should have same previous digits.\n");
            exit(0);
        }
    }
    else{
            printf("Error: Sum of last digit of both the number should be equal to 10.\n");
            exit(0);
        }
    return c;
}

int multiply_base_near_powerof10(int a, int b){
    int c,i=1, m= floor(log10(abs(a))) + 1, n = floor(log10(abs(b))) + 1;
    if(m==n){
        c= (a+b-pow(10,n))*pow(10,n);
        c+= (b-pow(10,n))*(a-pow(10,n));
    }
    else{
        if(m<n){
            n=m;
        }
        c= (b-pow(10,n))*(a-pow(10,n));
        if((-1*c)>pow(10,n)){
            for(i=2;i<10;i++){
                if((-1*c) < i*pow(10,n)){
                    c+= i*pow(10,n); break;
                }
            }
        }
        else{
            c+= pow(10,n);
        }
        c+= (a+b-pow(10,n)-i)*pow(10,n);
    }
    return c;
}

int multiply_equdigit_number(int a, int b){
    int c,x,y, m= floor(log10(abs(a))) + 1, n = floor(log10(abs(b))) + 1;
    if(m==n){
        if(m==2){
            x=a%10; y=b%10; a/=10; b/=10;
            c= (a*b)*100 + (a*y + b*x)*10 + (x*y);
        }
        else if(m==3){
            x=a%10; y=b%10; a/=10; b/=10;
            int u=a%10, v=b%10; a/=10; b/=10;
            c= (a*b)*10000 + (u*b + v*a)*1000 + (x*b + a*y + u*v)*100 + (u*y + v*x)*10 + (x*y);
        }
        else if(m==4){
            x=a%10; y=b%10; a/=10; b/=10;
            int u=a%10, v=b%10; a/=10; b/=10;
            int i=a%10, j=b%10; a/=10; b/=10;
             c=(a*b)*1000000 + (a*j + b*i)*100000 + (a*v +b*u + i*j)*10000 + (a*y +b*x + i*v + j*u)*1000 + (i*y + j*x + u*v)*100 + (u*y + v*x)*10 + (x*y);
        }
        else{
            printf("Error: Only valid for 2, 3 and 4 digit numbers.\n");
            exit(0);
        }
    }
    else{
        printf("Error: Number of digits need to be equal.\n");
        exit(0);
    }
    return c;
}