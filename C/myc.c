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
void boole_test(int x,int y,int z){
    if (x<3 && y>3)
        printf("ok\n");
    else if (x)
}

/*局部变量可以用任意类型相符的表达式来初始化，而全局变量只能用常量表达式初始化*/

int main(void){
    para_test();
    return 0;
}
