#!-*-coding:utf-8-*-
import sys
import time
import traceback
import socket

import SocketServer

class mysocket():

    def __init__(self,host='127.0.0.1',port=50007):
        self.host = host
        self.port = port

    def server(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #TCP方式

        #self.s.bind((self.host,self.port))
        self.s.bind(('',50007))
        self.s.listen(5)
        conn,addr = self.s.accept()
        try:
            print conn.recv(1024)
            conn.send("recv suc")
        except:
            pass
        finally:
            conn.close()
            self.s.close()

    def client(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #TCP方式
        try:
            self.s.connect((self.host,self.port))
            self.s.send("from {}".format(self.host))
            print self.s.recv(1024)
        except:
            pass
        finally:
            self.s.close()

class mytcpHandler_1(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print 'send from:{}'.format(self.client_address[0])
        print self.data
        self.request.send('recv suc')

class mytcpHandler_2(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.rfile.readlines().strip()
        print 'send from:{}'.format(self.client_address[0])
        print self.data
        self.wfile.write('recv suc')
        
class mysocketserver(mysocket):

    def __init__(self,host='127.0.0.1',port=50007):
        mysocket.__init__(self,host,port)

    def server(self):
        try:
            self.s = SocketServer.TCPServer(('',self.port),mytcpHandler_2)
            self.s.serve_forever()
        except:
            self.s.server_close()
        
        
        
       
       
if __name__  == "__main__":
    option = sys.argv[1]
    soc = mysocket()
#    soc = mysocketserver()
    if "server" == option:
        soc.server()
    elif "client" == option:
        soc.client()

"""
TCP发送数据时，已建立好TCP连接，所以不需要指定地址。UDP是面向无连接的，每次发送要指定是发给谁。
"""

