#-*-coding:utf-8-*-
#

""" you dao translation relaize in linux term , json type"""
import sys

from urllib import urlopen
import json

URL = "http://fanyi.youdao.com/openapi.do?keyfrom=terminal-trans&key=755551255&type=data&doctype=json&version=1.1&q="


errmsg = {
    20 : u"要翻译的文本过长",
    30 : u"无法进行有效的翻译",
    40 : u"不支持的语言类型",
    50 : u"无效的key",
    60 : u"无词典结果，仅在获取词典结果生效",
}

#import pdb
#pdb.set_trace()

def check_result(errorcode):
    if 0 == errorcode:
        return True
    else:
        return False

def print_list(listmsg):
    print " ".join(listmsg)

def print_dict(dictmsg):
    for key in dictmsg.keys():
        if "phonetic" in key:     #这个地方是音标
            continue
        print key + ": " + " ".join(dictmsg[key])

def trans(strs):

    full_url = URL + strs
    result =  urlopen(full_url).read()
    result_dict = json.JSONDecoder().decode(result)

    if not check_result(result_dict["errorCode"]):
        print str(result_dict["errorCode"]) + ": " + errmsg[result_dict["errorCode"]]
        return False

    #print_list(result_dict["translation"])

    print_dict(result_dict["basic"])

    print 


if __name__ == "__main__":
 
    #trans( " ".join(sys.argv[1:]))
    while True:
        words = raw_input()
        trans(words)
