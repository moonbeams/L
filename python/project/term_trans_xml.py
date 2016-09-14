#-*-coding:utf-8-*-
#encoding: utf-8
"""
#Note:youdao translation in linux terminal
#Author:wangzhaolei
#Date:
"""

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from urllib import urlopen
import os
#from xml.dom.minidom import parse
from xml.etree import ElementTree as et

MODE = 'brif'

URL = "http://fanyi.youdao.com/openapi.do?keyfrom=terminal-trans&key=755551255&type=data&doctype=xml&version=1.1&q="
#xmlfn = "x.xml"
def printlist(ls):
    str = u'' 
    for x in ls:
        str += x + ',  '
    print str[:-1]


def get_result(word):
    full_url = URL + word
    result = urlopen(full_url).read()
    #with open(xmlfn,'w') as fn:
    #    fn.write(result)
    return result

def result_parse(xmldata):
    #root = et.parse(xmlfile)
    root = et.fromstring(xmldata)
    for node in root.getchildren():
        if "errorCode" == node.tag:
            if '0' == node.text:
                pass
            elif '20' == node.text:
                pass #要翻译的文本过长
            elif '30' == node.text:
                pass #无法进行有效的翻译
            elif '40' == node.text:
                pass #不支持的语言类型
            elif '50' == node.text:
                pass #无效的key
            elif '60' == node.text:
                pass #无词典结果，仅在获取词典结果生效
        #elif "query" == node.tag:
        #    pass #输入内容
        #elif "translation" == node.tag:
        #    transres1 = node.getchildren()[0].text
        #    print transres1 + '\n'
        elif "basic" == node.tag:
            expl = []
            for ex in node.find("explains").getchildren():
                #print ex.text.encode('utf-8')
                expl.append(ex.text)
            if 'brif' != MODE:
                print "BASIC"
            printlist(expl)
        elif "web" == node.tag:
            if 'brif' == MODE:
                continue
            print "WEB"
            for webex in node.findall("explain"):
                print webex.find("key").text + ': ',
                printlist([x.text for x in webex.find("value").getchildren()])
    print 
                    


if __name__ == "__main__":
    #if '-b' == sys.argv[1]:
    #    MODE = 'brif'
    while True:
        word = raw_input()
        if word:
            result_parse(get_result(word))

