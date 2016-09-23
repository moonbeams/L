#myrm命令，执行时移动文件到~/.trash

#myrm -d  移动文件到trash 
#myrm -l  查看trash中的文件
#myrm -r  恢复trash中的文件


remvfile(){
    echo $@
    #mv $@ ~/.trash
}

to_array(){
    index=0
    declare -a array
    for i in "$@";do
        array[${index}]=${i}
        ((index++))
    done
    #echo  "${array[*]}"
}

case $1 in
-d)
    value=$(to_array $@)
    echo aa
    echo ${value}
    #remvfile $@
    ;;
-l)
    listfile
    ;;
-r)
    recofile
    ;;
esac

exit 0
