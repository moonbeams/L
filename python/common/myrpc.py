#-*-coding:utf-8-*-

"""RPC module, function whose name start with rpc_ can use this module """

from SimpleXMLRPCServer import SimpleXMLRPCServer
from xmlrpclib import ServerProxy

import sys
sys.path.append('/home/githubcode/L/python')

RPC_PORT = 9000

rpc_modules = [
    "test_func",
]

class rpc_server():

    def __init__(self,host='127.0.0.1'):
        self.server = SimpleXMLRPCServer(('0',RPC_PORT))

    def run(self):
        for module in rpc_modules:
            if "." in module:
                mod = eval("__import__(module).%s" % ".".join(module.split(".")[1:]) ) 
            else:
                mod = eval("__import__(module)")

            funcs = dir(mod)
            for x in funcs:
                if x.startswith("rpc_"):
                    self.server.register_function(eval("mod.%s" % x))
            self.server.serve_forever()

class rpc_client():
    
    def __init__(self,host='127.0.0.1'):
        self.client = ServerProxy('http://%s:%s' % (host,RPC_PORT))

    def run(self,func,*param):
        parstr = ",".join(str(x) for x in param)
        if parstr:
            cmd = "self.client.%s(%s)" % (func,parstr)
        else:
            cmd = "self.client.%s()" % func
        eval(cmd)


"""
    连接远端主机时报错socket.error: [Errno 113] No route to host
    原因：目标主机防火墙开启
          centos 7 关闭防火墙  systemctl stop firewalld 即可

"""
#rpcc = rpc_client("192.168.27.101")
#rpcc.run("add",3,4)

"""
    python动态加载模块
"""
#module = __import__("common.test").test
#module.rpc_printstr()


if __name__ == "__main__":

    option = sys.argv[1]
    if "server" == option:
        rpc_s = rpc_server()
        rpc_s.run()
    elif "client" == option:
        rpc_c = rpc_client()
        rpc_c.run("rpc_printstr")
    else:
        print "wrong argv"
