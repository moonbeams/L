#!/bin/bash

:<<!
变量：字母开头，不能有空格，可以使用_，不能使用标点符号，不能使用bash里面的关键字
    赋值表达式是等号两边不能有空格

    定义变量  xxx=
    输出。。  echo ${xxx}
    只读变量  readonly xxx
    删除变量  unset xxx

字符串:
    单引号：内容原样输出
    双引号：可以有变量，可以有转义字符
    反引号：执行命令
!

func_3(){
    var1="aaa"
    #str1="xxx,"$var1""
    str2="xxx,${var1}"
    echo $str1 $str2 
    echo ${#str2}         #获取字符串长度        
    echo ${str2:1:4}      #提取子字符串
    echo `expr index $str2 a`  #获取第一个下标
}

:<<!
数组：仅支持一维数组，下标从0开始
    定义：array=(v1 v2 v3)
          or
          array[0] = v1  ..

    读取：${array[0]}
          ${array[@/*]}  读取全部
          ${#array[@/*]} 数组长度
          ${#array[0]}   单个元素长度
          
!



#for
func(){
    for letter in A B C D;do
        echo "the letter is ${letter}xxx"    #变量加大括号是为了区分边界
    done
}


func_3