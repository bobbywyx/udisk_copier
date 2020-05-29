# -*- coding:utf-8 -*-
import os
from time import time
from datetime import datetime
import shutil

#  先读取设置   当前目录/copy/options.txt
local_path = os.getcwd()  # 当前程序所在目录
# print(local_path)
settings_list = []
txt_path = local_path + r'/copy/options.txt'  # 设置文件所在目录


def slicer(txtpath):  # 切片切出第一行，也就是采取的设置
    global lines
    with open(txtpath) as file:
        contents = file.read()
    string = ''
    for i in contents:
        if i != '\n':
            if i != '+':
                # print(i)
                string += i
            elif i == '+':
                settings_list.append(string)
                string = ''
        elif i == '\n':
            settings_list.append(string)
            string = ''
            break
    if string != '':
        settings_list.append(string)


slicer(txt_path)


# 测试路径是否可用双斜杠
# with open(settings_list[0]) as file:
#     contents = file.read()
# print(contents)

"""

1、刚刚options.txt里面有了各种设置，而且切片好了，这些设置放在settings_list里面
我觉得这些东西没有重新导入的必要，这样弄来弄去没意思，所以model里面就不要重新来过了
2、我需要的数据 第一次运行是没有日志的，所以没得用，但是以后就有了，所以第一步得创建日志，主要用来存放一些文件存储记录
后期用来查重还有一些更新的操作
所以很重要的一步就是记录日志，那么直接log.txt得了
3、不需要控制台，但是得能够停下来，手动加入快捷键有点浪费，所以打算同目录加入stop.txt，启动程序自动添加，如果这个文件被删除
程序停止
4、逻辑优先级

先把原来的数据理一下
path： 要复制的u盘的路径   就是盘符
time  ：可以按照时间选择复制，默认修改日期，可以选择不启用（全都要）向前或向后
size  ：按大小选择     默认全部     单位为mb  可以向上或向下选择
name  ：按名称选择   我还没想好这个东西有什么用   姑且不管他    打算按照关键字检索
suffix  ：按后缀选择    可以正向也可以反向  很好理解吧
deep  ：深拷贝   默认开启，遍历所有文件夹   关掉后只遍历第一层
smart  ：智能查重  这个功能打算使用的，就是估计会很垃圾2333
copy ：  白名单  里面写上u盘的名字或者序列号，就不会复制这些u盘

逻辑从先到后
path存在>copy>deep>time=size=name=suffix>smart


"""


#写入函数
def txtwriter(f_path,txt,aorw = 'w'):
    if aorw == 'w':
        with open(f_path, 'w') as f:
            f.write(txt)
    if aorw == 'a':
        with open(f_path, 'a') as f:
            f.write('\n'+txt)

#创建
txtwriter(local_path+r'/stop.txt',"")


class UdiscModel:
    """
    这个算是存储现当下和之后的所有u盘复制的记录啊之类的，还有读取目录信息文件信息
    name:
    last_copy_time：
    id：

    """
    def __init__(self,id, name='',last_copy_time = ''):
        self.name = name
        self.last_copy_time = last_copy_time
        self.id = id


class UdiscCtroller:
    def __init__(self):
        pass
    def main(self):
        while os.path.exists(local_path+r'/stop.txt'):
            pass

        else:
            pass
            # print(0)
