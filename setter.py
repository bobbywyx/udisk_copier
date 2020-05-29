import os
import time
# import this
def txtwriter(f_path,txt,aorw = 'w'):
    # f_path = r'E:\haha\readme.txt'
    if aorw == 'w':
        with open(f_path, 'w') as f:
            f.write(txt)
    if aorw == 'a':
        with open(f_path, 'a') as f:
            f.write('\n'+txt)
# print("notice that this program should be with copier.py in the same path")
print("the output of this program will be options.txt")
print("and do not edit options.txt manually")
print("the file and log and two programs(the other is copier) is suppposed to be in the same path")
print("if 'pathto is not given,things will go to where this program is'")
print(os.getcwd())
func_path = os.getcwd()

print(r'from what path ,example F:\ notice that there should not be blank between "\"and a letter')
print('tips:"from what path"means from what path the file you want to copy')
print("")
pathfrom = input("from what path:")
print(pathfrom)
print(r'to what path ,example E:\haha\options.txt notice that there should not be blank between "\"and a letter')
print('tips:"to what path"means the file"options.txt"(which is made by this program) will be')
print(r"the path must be end with '\options.txt'")
print("then the copier.py will make a folder under the path 'pathto'")
print("")
pathto = input("to what path:")
print(pathto)
if pathto=='':
    if os.path.exists(func_path+r'\copy'):
        pass
    else:
        os.mkdir(func_path+r'\copy')
    pathto=func_path+r'\copy'
    print("make dir successfully:"+pathto)

    if os.path.exists(pathto+r'\options.txt'):
        pass
    else:
        with open(pathto+r'\options.txt', 'w') as f:
            f.write('')
        print('make txt file successfully')
    pathto+=r'\options.txt'

txt = pathfrom +"+"+ pathto
# txtwriter(func_path+r'\read.txt',txt)


lines=0
def read(file_path):
    global lines
    # file_path=r'E:\haha\readme.txt'
    with open(file_path) as file:
        contents=file.read()
    # print(contents)
    if not contents=='':
        lines+=1

        for i in contents:
            # print(i,end='')
            if i == '\n':
                lines+=1
            # else:print('')
    else:
        lines=0
# read(func_path+r'\log.txt')
read(pathto)
# print(lines)


class OptionModel():
    """
    id:  某设置的id  不唯一，会改变
    path： 要复制的u盘的路径   就是盘符
    time  ：可以按照时间选择复制，默认修改日期，可以选择不启用（全都要）向前或向后
    size  ：按大小选择     默认全部     单位为mb  可以向上或向下选择
    name  ：按名称选择   我还没想好这个东西有什么用   姑且不管他    打算按照关键字检索
    suffix  ：按后缀选择    可以正向也可以反向  很好理解吧
    deep  ：深拷贝   默认开启，遍历所有文件夹   关掉后只遍历第一层
    smart  ：智能查重  这个功能打算使用的，就是估计会很垃圾2333
    copy ：  白名单  里面写上u盘的名字或者序列号，就不会复制这些u盘
    """
    def __init__(self,id=0,path ='',select_time='',select_size='',select_name='',select_suffix='',select_deep='',select_smart='',select_copy=''):
        self.id = id
        self.path = path
        self.select_time   = select_time
        self.select_size   = select_size
        self.select_name   = select_name
        self.select_suffix = select_suffix
        self.select_deep   = select_deep
        self.select_smart  = select_smart
        self.select_copy   = select_copy


class OptionManagerController():
    id = 0

    def __init__(self):
        self.Option_list = []
    @property
    def Opt_list(self):
        return self.Option_list
    def id_creater(self):
        OptionManagerController.id +=1

        return OptionManagerController.id
    def add_opt(self,opt):
        opt.id = self.id_creater()
        # print(stu_info)
        # print(stu_info.age)
        # print(stu_info.id)
        self.Option_list.append(opt)
    def del_Opt(self,id):
        for i in self.Option_list:
            if i.id == id:
                self.Option_list.remove(i)
    def update_stu(self,opt_info):
        for i in self.Option_list:
            if i.id == opt_info.id:
                '''time  
                    size  
                    name  
                    suffix
                    deep  
                    smart 
                    copy  
                    '''
                i.path = opt_info.path
                i.time = opt_info.time
                i.size = opt_info.size
                i.name = opt_info.name
                i.suffix = opt_info.suffix
                i.deep = opt_info.deep
                i.smart = opt_info.smart
                i.copy = opt_info.copy
class OptionManagerView():
    def __init__(self):
        self.__manager = OptionManagerController()
    def __home_page_printer(self):
        print("1)添加设置")
        print("2)查询设置")
        print("3)修改设置")
        print("4)删除设置")
        print("5)确认设置")
        print("6)导入设置（建议选上）")
        print("7)退出")
    def __select_menu(self):
        i = input("请输入")
        if i =='1':
            self.__add_info()
        elif i =='2':
            print(OptionModel)
            self.__print_opt_info(self.__manager.Opt_list)
        elif i =='3':
            self.__change_opt()
        elif i =='4':
            self.__del_opt()
        elif i =='5':
            self.__select()
        elif i =='6':
            self.__add_info_list()
        elif i =='7':
            print("3秒后即将退出。。。。。。")
            time.sleep(3)
            exit()
        else:print('错误')
    def main(self):
        while True:
            self.__home_page_printer()
            self.__select_menu()
    def __add_info(self):
        path = pathfrom
        time = input('time')
        size = input('size')
        name =input('name')
        suffix = input('suffix')
        deep = input('deep')
        smart = input('smart')
        copy = input('copy')
        stu = OptionModel(path=path,select_time=time,select_size=size,select_name=name,select_suffix=suffix,select_deep=deep,select_smart=smart,select_copy=copy)
        self.__manager.add_opt(stu)
    def __add_info_list(self):
        global idlist
        a= 0
        for i in idlist:
            path = idlist[a][0]
            time = idlist[a][1]
            size = idlist[a][2]
            name = idlist[a][3]
            suffix = idlist[a][4]
            deep = idlist[a][5]
            smart = idlist[a][6]
            copy = idlist[a][7]
            stu = OptionModel(path=pathfrom,select_time=time, select_size=size, select_name=name, select_suffix=suffix, select_deep=deep,
                              select_smart=smart, select_copy=copy)
            self.__manager.add_opt(stu)
            a+=1
    def __print_opt_info(self,list_for_print):
        for i in list_for_print:
            print('id',i.id)
            print('time set',i.select_time)
            print('size set',i.select_size)
            print('')
            # print('sex',i.sex)
            # print('age',i.age)
            # print('score',i.score)
    def __change_opt(self):
        print("-------此功能未完成-------")
        pass
    def __del_opt(self):
        i = input('del id')
        self.__manager.del_Opt(i)
    def __select(self,):
        def codemaker(id):
            codeout = self.__manager.Opt_list[int(id)].path + '+' +self.__manager.Opt_list[int(id)].select_time + '+' + self.__manager.Opt_list[int(id)].select_size + '+' + self.__manager.Opt_list[int(id)].select_name + '+' + self.__manager.Opt_list[int(id)].select_suffix+ '+' + self.__manager.Opt_list[int(id)].select_deep + '+' + self.__manager.Opt_list[int(id)].select_smart + '+' + self.__manager.Opt_list[int(id)].select_copy
            return codeout
        id1 = int(input('select id'))-1
        # code = self.__manager.Opt_list[int(id1)].select_time + '+' + self.__manager.Opt_list[int(id1)].select_size + '+' + self.__manager.Opt_list[int(id1)].select_name + '+' + self.__manager.Opt_list[int(id1)].select_suffix+ '+' + self.__manager.Opt_list[int(id1)].select_deep + '+' + self.__manager.Opt_list[int(id1)].select_smart + '+' + self.__manager.Opt_list[int(id1)].select_copy
        code = codemaker(id1)
        print("确认为："+code)
        txtwriter(pathto,code)
        for i in range(len(self.__manager.Opt_list)):
            if i!=id1:
                code = codemaker(i)
                txtwriter(pathto,code,'a')



# manager = StudentManagerController()
# manager.add_stu(StudentModel('小老鼠01'))
# print(StudentModel('aa').id)
# manager.add_stu(StudentModel('小老鼠02'))
# manager.del_stu(1)
# for i in manager.stu_list:
#     print(i.name)

idlist = []

def slicer(txtpath):
    global lines
    with open(txtpath) as file:
        contents = file.read()
    for i in range(lines):
        idlist.append([])
    string = ''
    a = 0
    for i in contents:
        # print('a'+str(a))
        if i != '\n':
            if i != '+':
                string +=i
            elif i == '+':
                idlist[a].append(string)
                string = ''


        # print(len(idlist[a]))
        # if len(idlist[a]) == 7:
        #     a+=1
        #     print('yes')

        elif i == '\n':
            idlist[a].append(string)
            a+=1
            string = ''
    if string!='':
        idlist[a].append(string)
    print(idlist)
slicer(pathto)

view = OptionManagerView()
view.main()

