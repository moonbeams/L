#include <stdio.h>

#include <math.h>


void print_percentage(void){
    int charnum;
    charnum = printf("%%abcd\n");    
    printf("%d",charnum);   /*printf 返回打印字符数,\n也算一个*/
}

/*
 如果一个声明同时也要求分配存储空间，则称为定义

 char firstletter;    定义
 firstletter = 'a';   初始化
 char secondletter = 'b'; 定义同时初始化
 */

/*
 调用math.h的函数时，编译需 gcc -lm xxx,因为math.h在libm.so中，增加选项告知搜索路径
 -lc不用加，一般函数在libc.so库中，gcc默认选项
 */
void math_test(void){
    double pi = 3.1416;
    printf("sin(pi/2)=%f",sin(pi/2));
}

void increment(int x){
    x = x + 1;    
}

void para_test(void){
    int i = 1;
    increment(i);
    printf("%d",i);
}

/* 布尔运算: && || !  */

/* case 后必须跟常量表达式，同全局表量，编译时需要计算出值 */
void switch_test(int day){
    switch(day){
    case 1:
        printf("Monday\n");
        break;
    case 2:
        printf("Tuesday\n");    
        break;
    }    
}


void print_logrithm(double x){
    if (x <= 0.0){
        printf("need positive number!\n");
        return;
    }    
    printf("The log of x is %f",log(x));
}


/* int函数没有返回值   编译时加-Wall参数可以检测到 */
void is_leap_year(int year){
    if ((!(year % 4) && (year % 100)) || !(year % 400)) 
        printf("%d is leap year\n",year);
    else
        printf("%d is not leap year\n",year);
}


/* 递归-阶乘  注意定义base case */
int factorial(int n){
    if (n == 0)
        return 1;
    else{
        int recurse = factorial(n-1);
        int result = n * recurse;
        return result;
    }    
}

void xx(int a,int b){
    if (a % b == 0)
        printf("%d",b);
    else
        xx(b,a%b);
}


int factorial_while(int n){
    int result = 1;
    while (n>0){
        result *= n;
        n = n-1;
    }    
    return result;
}

int factorial_dowhile(int n){
    int result = 1;
    do{
        result *= n;
        n = n-1;  
    }while(n>0);
    return result;
}

int factorial_for(int n){
    return ;
}

/*局部变量可以用任意类型相符的表达式来初始化，而全局变量只能用常量表达式初始化*/

int main(void){
    int result = factorial_dowhile(5);
    printf("%d",result);
    return 0;
}
