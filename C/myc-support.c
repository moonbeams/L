#include <stdio.h>

#include <stdlib.h>
#include <string.h>

/* string */
char *str_join(char *str1,char *str2){
    char *str3 = (char *) malloc(strlen(str1)+strlen(str2)+1);
    if (str3 == NULL)
        exit(1);      // exit(1)发生异常直接退出程序，exit(0)正常退出；
                      // exit()能够在退出前把缓冲里的文件写回，而_exit()直接退出
    char *tempc = str3;
    while(*str1 != '\0'){
        *str3 ++ = *str1 ++; 
    }
    while(*str2 != '\0'){
        *str3 ++ = *str2 ++;
    }
    return tempc;
}


int main(void){
    char *new_str = str_join("aaa","bbb");
    printf("%s",new_str);

    free(new_str);    //使用malloc申请内存之后，需要释放，否则这块内存将无法再使用，出现内存泄露
    new_str = NULL;
    return 0;
}
