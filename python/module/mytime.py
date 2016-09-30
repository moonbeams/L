#-*-coding:utf-8-*-
import time

"""
    时间戳：相对于1970.1.1 00:00:00以秒计算的偏移量
    struct time: year (four digits, e.g. 1998)
                 month (1-12)
                 day (1-31)
                 hours (0-23)
                 minutes (0-59)
                 seconds (0-59)
                 weekday (0-6, Monday is 0)
                 Julian day (day in the year, 1-366)
                 DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时
                     If the DST flag is 0, the time is given in the regular time zone;
                     if it is 1, the time is given in the DST time zone;
                     if it is -1, mktime() should guess based on the date and time.
                 
                 UTC + 时区差 ＝ 本地时间 
                 时区差东为正，西为负。在此，把东八区时区差记为 +0800， 
                 UTC + (＋0800) = 本地（北京）时间 (1) 

"""

print time.time()

"""
print time.clock()   #???
time.sleep(1)
print time.clock()
time.sleep(1)
print time.clock()
"""

#事件戳(默认为当前时间) --> 字符串'Sat Mar 28 22:24:24 2009'
print time.ctime(time.time()) 

#时间戳 --> UTC时区struct time
print time.gmtime()

#时间戳 --> 当地时区struct time
print time.localtime()

#struct time --> 字符串
print time.asctime()

#struct time --> 时间戳
print time.mktime(time.localtime())

"""
    python中时间日期格式化符号：
        %y 两位数的年份表示（00-99）
        %Y 四位数的年份表示（000-9999）
        %m 月份（01-12）
        %d 月内中的一天（0-31）
        %H 24小时制小时数（0-23）
        %I 12小时制小时数（01-12）
        %M 分钟数（00=59）
        %S 秒（00-59）
         
        %a 本地简化星期名称
        %A 本地完整星期名称
        %b 本地简化的月份名称
        %B 本地完整的月份名称
        %c 本地相应的日期表示和时间表示
        %j 年内的一天（001-366）
        %p 本地A.M.或P.M.的等价符
        %U 一年中的星期数（00-53）星期天为星期的开始
        %w 星期（0-6），星期天为星期的开始
        %W 一年中的星期数（00-53）星期一为星期的开始
        %x 本地相应的日期表示
        %X 本地相应的时间表示
        %Z 当前时区的名称
        %% %号本身 
"""
#struct time(默认当地时间) --> 格式化字符串
print time.strftime("%Y-%m-%d %H-%M-%S",time.localtime())

#格式化字符串 --> struct time
print time.strptime("2009-03-20 11:45:39","%Y-%m-%d %H:%M:%S")
