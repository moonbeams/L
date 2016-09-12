# -*- coding:utf-8 -*-

"""wx note"""

import sys
import time
import wx

"""
最小的空wxpython
使用OnInit 会自动调用wx.App的init
"""
class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None,title='wx')
        frame.Show()
        return True


"""
自己定义init
"""
class App_1(wx.App):
    def __init__(self):
        wx.App.__init__(self)
        self.frame = wx.Frame(parent=None,title='wx')
        self.frame.Show()
        
"""
image
"""
class Frame(wx.Frame):
    def __init__(self,image,parent=None,id=-1,pos=wx.DefaultPosition,title="hellowxpython"):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        self.bmp = wx.StaticBitmap(parent=self,bitmap=temp)
     
class App_2(wx.App):
    def OnInit(self):                  #wxpython 自动调用OnInit
        image = wx.Image("wxpython.jpg",wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)  #应用程序的主顶级窗口，不设置的话默认第一个顶级窗口为主
        return True

"""
SimpleApp
"""
"""
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = wx.Frame(None)
    frame.Show(True)
    app.MainLoop()
"""

"""
redirect
生成两个框，一个自动生成的wxpython:sys.std.... 一个是代码中写的frame，可分离
"""
class Frame_3(wx.Frame):
    def __init__(self,parent,id,title):
        print "Frame __init__"
        wx.Frame.__init__(self,parent,id,title)
class App_3(wx.App):
    def __init__(self,redirect=True,filename=None):    #如果定义了filename，则输出会定向到文件中,且不会生成重定向窗口
        print "App __init__"    #此处依然打印到终端，不在wx.App对象控制流内
        wx.App.__init__(self,redirect,filename)
    def OnInit(self):                        #有__init__，wxpyhton依然会自动调用OnInit
        print "OnInit"
        self.frame = Frame_3(None,-1,'redirect')
        self.frame.Show()
        self.SetTopWindow(self.frame)
        print >> sys.stderr,"error"
        return True
    def OnExit(self):        #也是自动调用，在关闭最后一个顶层窗口--无parent的窗口，可用来自定义清理工作
        print "OnExit"
        #time.sleep(5)     窗口依然立即消失，但是程序没有退出，执行5s延时

"""
exit
"""
class Frame_4(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
class App_4(wx.App):
    def __init__(self,redirect=True,filename="output"):
        wx.App.__init__(self,redirect,filename)
        self.frame = Frame_4(None,-1,"test")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        self.SetExitOnFrameDelete(False)  #设置为false之后窗口关闭程序依然不退出，除非wx.Exit()被调用
                                          #目前还不知道用在哪
    def OnExit(self):
        print "Exit"

"""
Frame:
wx.Frame(parent, id=-1, title=””, pos=wx.DefaultPosition,
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE,
        name=”frame”)
parent：父窗口，顶级窗口为None。子窗口随父窗口销毁而销毁，被限制在父窗口内移动缩放
id：-1时自动生存一个id号
title：
pos：wx.Point对象，指定窗口左上角的位置，(0,0)为显示器的左上角，默认(-1,-1)表示由系统选择
size：wx.Size对象，初始尺寸，默认(-1,-1)
stype：？？
name：框架内在的名字，可以用来寻找窗口？？

id 可使用wx.NewId()创建，frame.GetId()获取，且避免使用wx.ID_LOWEST和wx.ID_HIGHEST之间的id
style：
    wx.DEFAULT_FRAME_STYLE = wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESZIE_BORDER |
                             wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
    如果要去掉缩放和改变窗口尺寸：
    wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX)

    wx.CAPTION：框架上增加标题栏，显示该框架的标题属性。
    wx.CLOSE_BOX：标题栏上显示一个关闭框。
    wx.FRAME_SHAPED：用这个创建框架之后可以使用SetShape()去创建一个非矩形窗口
    wx.FRAME_TOOL_WINDOW：通过给框架一个比正常更小的标题栏,使框架看起来像一个工具框窗口。在Windows下,使用这个样式创建的框架不会出现在显示                          所有打开窗口的任务栏上。  ？？
    wx.MAXISIZE_BOX：最大化框
    wx.MINISIZE_BOX：最小化框
    wx.RESIZE_BORDER：可以改变尺寸的边框
    wx.SIMPLE_BORDER：没有装饰的边框，有平台限制
    wx.SYSTEM_MENU:增加系统菜单(带有关闭、移动、改变尺寸等功能)和关闭框到这个窗口(鼠标右键点击标题栏)。在系统菜单中的改变尺寸和关闭功能的有
                   效性依赖于wx.MAXIMIZE_BOX, wx.MINIMIZE_BOX和wx.CLOSE_BOX样式是否被应用

"""
"""
style test
"""
class App_5(wx.App):
    def OnInit(self):
        #self.frame = wx.Frame(None,-1,"style",style=wx.DEFAULT_FRAME_STYLE^(wx.SYSTEM_MENU))
        #self.frame = wx.Frame(None,-1,"style",style=(wx.FRAME_TOOL_WINDOW | wx.CAPTION | wx.CLOSE_BOX))
        self.frame = wx.Frame(None,-1,"style",style=(wx.CAPTION | wx.HELP.FRAME_EX_CONTEXTHELP))
        self.frame.Show()
        return True

"""
button event
"""
class App_6(wx.App):
    def __init__(self,redirect=True,filename=None):
        wx.App.__init__(self,redirect,filename)
        self.frame = wx.Frame(None,-1,"buttonevent",size=(300,100))
        self.panel = wx.Panel(self.frame)           #wx.Panel将创建一个和frame大小一样的panel实例，panel内的元素可通过tab键遍历
        self.button = wx.Button(self.panel,label="close",pos=(125,10),size=(50,50))

        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,self.button)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWin)
        self.frame.Show()
    def OnCloseMe(self,event):
        print "close by button"
        self.frame.Close(True)
    def OnCloseWin(self,event):
        print "close by x"
        self.Destroy()

"""
tool bar
"""
class Frame_7(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(300,200))
        panel = wx.Panel(self)
        statusbar = self.CreateStatusBar()
        #toolbar = self.CreateToolBar()
        #toolbar.AddSimpleTool(wx.NewId(), wx.Bitmap("test.jpg",type=wx.BITMAP_TYPE_JPEG),
        #                "New", "Long help for 'New'") 
        #toolbar.Realize()
        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menubar.Append(menu1,"&file")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(),"&copy","copy in status bar")
        menu2.Append(wx.NewId(),"&cut","")
        menu2.Append(wx.NewId(),"&paste","")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(),"&option","display option")
        menubar.Append(menu2,"&edit")
        self.SetMenuBar(menubar)
class App_7(wx.App):
    def __init__(self,redirect=True,filename=None):
        wx.App.__init__(self,redirect,filename)
        self.frame = Frame_7(None,-1,"tools")
        self.frame.Show()

"""
message dialog
"""
#wx.MessageDialog(parent,message,caption="Message box",style=wx.OK | wx.CANCEL,pos=wx.DefaultPosition)
class Frame_8(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title,size=(300,200))
        self.panel = wx.Panel(self)
        self.Bind(wx.EVT_CLOSE,self.closewin)
    def closewin(self,event):
        #dlg parent 不能使用self.frame，原因暂时不明;可使用None，即与原来的窗口分离
        dlg = wx.MessageDialog(self.panel,"close window?","",wx.YES_NO | wx.ICON_QUESTION)
        #返回值为整数，[ wx.ID_YES,wx.ID_NO,wx.ID_OK,wx.ID_CANCEL ]
        result = dlg.ShowModal()
        if 5103 == result:
            self.Destroy()
        else:
            dlg.Destroy()
#文本输入对话框
class Frame_8_1(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel,label="print",pos=(125,10),size=(50,50))
        self.Bind(wx.EVT_BUTTON,self.printstr,self.button)
    def printstr(self,event):
        #实测使用filename时，dialog中只有框架关闭时会一次性打印所有数据
        #此例中点了n次ok，会在关闭框架时向文件写入n个yes
        #如果此函数被绑定上EVT_CLOSE，经实测文件中不会写入数据
        dlg = wx.TextEntryDialog(self.panel,"close window?","","yes")
        if dlg.ShowModal() == wx.ID_OK:
            print dlg.GetValue()
        #result= dlg.ShowModal()
        #print result
#列表选择
class Frame_8_2(Frame_8_1):
     def __init__(self,parent,id,title):
         Frame_8_1.__init__(self,parent,id,title)
     def printstr(self,event):
         dlg = wx.SingleChoiceDialog(self.panel,"what version?","single choice",['centos','ubuntu','read hat'])
         if dlg.ShowModal() == wx.ID_OK:
             print dlg.GetStringSelection()
class App_8(wx.App):
    def __init__(self,redirect=False,filename="output"):
        wx.App.__init__(self,redirect,filename)
        self.frame = Frame_8_2(None,-1,"")
        self.frame.Show()

"""
    EVENT
    wx.MouseEvent:wx.EVT_LEFT(MIDDLE/RIGHT)_DOWN, wx.EVT_LEFT(MIDDLE/RIGHT)_UP, wx.EVT_LEFT(MIDDLE/RIGHT)_DCLICK
                  wx.EVT_MOTION 用户鼠标移动
                  wx.EVT_ENTER(LEAVE)_WINDOW 鼠标移入(移出)窗口
                  wx.EVT_MOUSEWHEEL 鼠标滚轮
                  wx.EVT_MOUSE_EVENTS 可绑定所有的鼠标事件
    wx.CommandEvent: wx.EVT_BUTTON wx.EVT_MENU....

    Bind(event,handler,source=None,id=wx.ID_ANY,id2=wx.ID_ANY)

"""
class Frame_9(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menu1item = menu1.Append(wx.NewId(),"&Exit")
        menubar.Append(menu1,"&File")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU,self.OnCloseMe,menu1item)
    def OnCloseMe(self,event):
        self.Close(True)
class App_9(wx.App):
    def OnInit(self):
        self.frame = Frame_9(self,None,-1,"menuevt")
        self.frame.Show()


if __name__ == "__main__":
    app = App_9()
    app.MainLoop()

















