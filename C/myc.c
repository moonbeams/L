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


/*局部变量可以用任意类型相符的表达式来初始化，而全局变量只能用常量表达式初始化*/

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

/* int i=1 此种定义时i为for的局部变量，且编译需要-std=c99  C语言中不推荐这种写法，兼容性问题 */
int factorial_for(int n){
    int result = 1;
    for(int i=1;i<=n;i++){
        result *= i;
    }
    return result;
}


/* 此程序中i，j只能再for中定义，若在之前定义就是这个函数内部的局部变量，在一次for循环结束是不会释放 */
void print_99(void){
    int i,j;
    for(i=1;i<=9;i++){
        for(j=1;j<=i;j++)
            printf("%d  ",i*j);
        printf("\n");    
    }
}

/* 结构体  */
/* 
 * 定义在函数外部：struct complex_struct {double x,y;};     //定义tag
 *                 int main(void){
 *                     struct complex_struct z;       //定义变量
 *                 } 
 * 结构体变量定义时初始化：struct complex_struct z = {3.0,4.0};
 *
 *  double x =3.0;
 *  struct complex_struct z1={x,4.0,} //z1.x=3.0,z1.y=4.0
 *  struct complex_struct z2={3.0}   //z1.x=3.0,z1.y=0.0
 *  struct complex_struct z3={}      //z1.x=0.0,z1.y=0.0
 *  
 *  结构体赋值：全局变量只能用常量，
 *              不能使用这种方式：
 *                  struct complex_struct z1;
 *                  z1={3.0,4.0};
 *              结构体之间赋值可以：
 *                  struct complex_struct z1 = {3.0,4.0};
 *                  struct complex_struct z2 = z1;
 *                  z1 = z2;
 *
 *  结构体可以作为函数参数以及函数返回值 */
void struct_test(void){
    struct complex_struct { double x,y;} z;
    double x = 3.0;
    z.x = x;
    z.y = 4.0;
    if(z.y<0)
        printf("z=%.1f%.1fi\n",z.x,z.y);
    else
        printf("z=%.1f+%.1fi\n",z.x,z.y);
}


struct complex_struct {double x,y;};           //必须在所有调用的前面定义，否则 :parameter 1 (‘z1’) has incomplete type

struct complex_struct add_complex(struct complex_struct z1,struct complex_struct z2){
    z1.x = z1.x + z2.x;
    z1.y = z1.y + z2.y;
    return z1;    
}

int main(void){
    struct complex_struct z = {3.0,4.0};
    z = add_complex(z,z);
    printf("z=%.1f+%.1fi",z.x,z.y);
    return 0;
}
