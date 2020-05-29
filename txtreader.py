lines=0
path = ''
def read(file_path):
    global lines
    # file_path=r'E:\haha\readme.txt'
    with open(file_path) as file:
        contents=file.read()
    print(contents)
    if not contents=='':
        lines+=1

        for i in contents:
            # print(i,end='')
            if i == '\n':
                lines+=1
            else:print('')
    else:
        lines=0
read(r'D:\文件\projects\yyy\信息课无聊\code\copier\copy\options.txt')
print(lines)