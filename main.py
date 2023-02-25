import getpass
import time as t
import os
import sys
import platform
import shutil
import webbrowser
import keyboard as kb
import re
import assistant.clicker as clicker
import assistant.imgviewer as imgviewer
import assistant.bigtools.file_processer as fp

ALLCMD = [
        "cls","CLS",
        "time","TIME",
        "ver","VER",
        "exit","EXIT",
        "help","HELP",
        "tree","TREE",
        "type","TYPE",
        "rename","RENAME","ren","REN",
        "md","MD","mkdir","MKDIR",
        "rd","RD","rmdir","RMDIR",
        "rmdirall","RMDIRALL",
        "calc","CALC",
        "update","UPDATE",
        "start","start",
        "absp","ABSP",
        "rep","REP",
        "cd","CD",
        "edit","EDIT",
        "clicker","CLICKER",
        "imgviewer","IMGVIEWER",
        "stmt","STMT",
        "fp","FP"
        ]

def splitdir(path):
    pathlist = path.split("\\")
    last = pathlist[len(pathlist)-1]
    newpath = path.strip(last)
    return newpath
    
def tree(path,level):
    def getFileStr(level):#文件
        return '  '*level+'- '
    def getDicStr(level):#文件夹
        return '  '*level+'+'
    def printFile(path,level):
        if os.path.exists(path):
            try:
                files = os.listdir(path)
            except PermissionError:
                print('  '*level+"没有权限 拒绝访问")
            else:
                for f in files :
                    subpath=os.path.join(path,f)
                    if os.path.isfile(subpath):
                        print(getFileStr(level)+os.path.basename(subpath))
                    else:
                        leveli=level+1
                        print(getDicStr(level)+os.path.basename(subpath))
                        printFile(subpath,leveli)
    printFile(path,level)

thepath = "absp"
user = "C:\\Users\\" + getpass.getuser()
print("Easy Command [版本 1.21.13]\n简易版CMD\n第一次使用建议输入help和update\n\n")
times = 1
while True:
    aduser = user+"\\"
    if times == 1:
        command = str(input(user+">"))
    if times > 1:
        print("\n")
        command = str(input(user+">"))
    times = times + 1
    cmdlist = []
    if " " in command:
        while True:
            if command.find(" ") == len(command)-1:
                command = command[0:-1]
            if command.find(" ") == 0:
                command = command[1:len(command)+1]
            else:
                break
        cmdlist = command.split()
    else:
        cmdlist.append(command)
    try:
        if "/?" in cmdlist:
            if "/?" in cmdlist[0]:
                print("'/?'不是一个命令")
        elif "" == command:
            times = 1
            pass
        elif "cls" == cmdlist[0] or "CLS" == cmdlist[0]:
            print("\033c",end="")
            times = 1
        elif "time" == cmdlist[0] or "TIME" == cmdlist[0]:
            time = t.ctime()
            print("当前时间："+time[11:19])
        elif "ver" == cmdlist[0] or "VER" == cmdlist[0]:
            print(platform.platform())
        elif "exit" == cmdlist[0] or "EXIT" == cmdlist[0]:
            print("\033c",end="")
            sys.exit()
        elif "tree" == cmdlist[0] or "TREE" == cmdlist[0]:
            if len(cmdlist) > 2:
                print("参数太多 - "+cmdlist[1])
            elif len(cmdlist) == 1:
                tree("C:\\",1)
            elif len(cmdlist) == 2:
                if thepath == "rep":
                    path = aduser + cmdlist[1]
                else:
                    path = cmdlist[1]
                tree(path,1)
        elif "type" == cmdlist[0] or "TYPE" == cmdlist[0]:
            if len(cmdlist) == 1:
                print("命令语法不正确")
            elif len(cmdlist) == 2:
                if thepath == "rep":
                    file = aduser + cmdlist[1]
                else:
                    file = cmdlist[1]
                try:    
                    read = open(file,"r",encoding="utf-8")
                    print(read.read())
                except FileNotFoundError:
                    print("没有此文件")
                except PermissionError:
                    print("此路径指向文件夹，或无权限访问")
        elif cmdlist[0] in ["rename","RENAME","ren","REN"]:
            if len(cmdlist) < 3 or len(cmdlist) > 3:
                print("命令语法不正确")
            if len(cmdlist) == 3:
                if thepath == "rep":
                    path = aduser + cmdlist[1]
                else:
                    path = cmdlist[1]
                newpath = splitdir(path)
                newname = cmdlist[2]
                new = newpath + newname
                os.rename(path,new)
        elif cmdlist[0] in ["md","MD","mkdir","MKDIR"]:
            if len(cmdlist) < 2 or len(cmdlist) > 2:
                print("命令语法不正确")
            if len(cmdlist) == 2:
                if thepath == "rep":
                    path = aduser + cmdlist[1]
                else:
                    path = cmdlist[1]
                try:
                    os.mkdir(path)
                except FileExistsError:
                    print("子目录已经存在")
                except FileNotFoundError:
                    print("系统找不到指定路径")
                except OSError:
                    print("路径有错误")
        elif cmdlist[0] in ["rd","RD","rmdir","RMDIR"]:
            if len(cmdlist) < 2 or len(cmdlist) > 4:
                print("命令语法不正确")
            if len(cmdlist) >= 2 and len(cmdlist) <= 4:
                if command.count('"') == 2:
                    cmdlist = cmdlist[0:3]
                    path = re.findall('"(.*?)"',command)[0]
                    cmdlist.append(path)
            if len(cmdlist) == 3:
                if cmdlist[1] not in ["/s","/q","/S","/Q"]:
                    no = cmdlist[1]
                    no = no[1:]
                    print("无效开关 - "+no)
                elif cmdlist[1] in ["/s","/S"]:
                    if thepath == "rep":
                        path = aduser + cmdlist[2]
                    else:
                        path = cmdlist[2]
                    while True:
                        ans = input(path+"，是否确认（Y/N）？：")
                        if ans not in ["Y","N"]:
                            pass
                        if ans == "Y":
                            try:
                                shutil.rmtree(path)
                            except FileNotFoundError:
                                print("系统找不到指定路径")
                            finally:
                                break
                        if ans == "N":
                            break
            if len(cmdlist) == 4:
                if cmdlist[1] not in ["/s","/S"]:
                    no = cmdlist[1]
                    print("无效开关："+no.strip("/"))
                elif cmdlist[2] not in ["/q","/Q"]:
                    no = cmdlist[2]
                    print("无效开关："+no.strip("/"))
                else:
                    if thepath == "rep":
                        path = aduser + cmdlist[3]
                    else:
                        path = cmdlist[3]
                    try:
                        shutil.rmtree(path)
                    except FileNotFoundError:
                        print("系统找不到指定路径")
            if len(cmdlist) == 2:
                if thepath == "rep":
                    path = aduser + cmdlist[1]
                else:
                    path = cmdlist[1]
                try:
                    os.removedirs(path)
                except FileNotFoundError:
                    print("系统找不到指定路径")
                except OSError:
                    print("文件夹不是空的\n可使用ECD专有命令rmdirall或在此命令加上/s")
        elif "rmdirall" == cmdlist[0] or "RMDIRALL" == cmdlist[0]:
            if len(cmdlist) < 2 or len(cmdlist) > 2:
                if command.count('"') == 2:
                    cmdlist = cmdlist[0:1]
                    path = re.findall('"(.*?)"',command)[0]
                    cmdlist.append(path)
                else:    
                    print("命令语法不正确")
            if len(cmdlist) == 2:
                if thepath == "rep":
                    path = aduser + cmdlist[1]
                else:
                    path = cmdlist[1]
                try:
                    shutil.rmtree(path)
                except FileNotFoundError:
                    print("系统找不到指定路径")
        elif "calc" == cmdlist[0] or "CALC" == cmdlist[0]:
            os.system("calc.exe")
        elif "update" == cmdlist[0] or "UPDATE" == cmdlist[0]:
            txt = open("版本更新.txt","r",encoding="utf-8")
            txt = txt.read()
            print("\n"+txt)
        elif "start" == cmdlist[0] or "START" == cmdlist[0]:
            if len(cmdlist) == 1:
                os.system("start cmd")
            else:
                file = cmdlist[1]
                try:
                    url = file.split(".")
                    if len(url) == 3:
                        if url[0] == "www":
                            webbrowser.open(file)
                    else:
                        raise SyntaxError
                except:
                    if thepath == "absp":
                        os.system("start "+file)
                    if thepath == "rep":
                        os.system("start "+aduser+file)
        elif "absp" == cmdlist[0] or "ABSP" == cmdlist[0]:
            thepath = "absp"
            print("设定成功，路径设定变为绝对路径")
        elif "rep" == cmdlist[0] or "REP" == cmdlist[0]:
            thepath = "rep"
            print("设定成功，路径设定变为相对路径，上级路径为:"+user)
        elif "cd" == cmdlist[0] or "CD" == cmdlist[0] or "chdir" == cmdlist[0] or "CHDIR" == cmdlist[0]:
            if len(cmdlist) == 1:
                print(user)
            if len(cmdlist) == 2:
                if thepath == "absp":
                    user = cmdlist[1]
                if thepath == "rep":
                    user = aduser + cmdlist[1]
            if len(cmdlist) > 2:
                print("参数过多")
        elif "edit" == cmdlist[0] or "EDIT" == cmdlist[0]:
            print("1:当前目录名为："+user)
            print("2:当前路径模式为："+thepath,end="")
            if thepath == "absp":
                print("（绝对路径）")
            elif thepath == "rep":
                print("相对路径")
            mode = input("请输入想要更改的序号（输入其他字符退出）:")
            if mode == "1":
                mod = input("请输入想要更改的目录名（输入exit退出）:")
                if mod == "exit":
                    pass
                else:
                    user = mod
            if mode == "2":
                mod = input("更改成绝对路径输入1，相对路径输入2，其他字符退出：")
                if mod == "1":
                    thepath = "absp"
                elif mod == "2":
                    thepath = "rep"
        elif "clicker" == cmdlist[0] or "CLICKER" == cmdlist[0]:
            if len(cmdlist) == 1:
                input("按下任意键开始")
                print("连点开始")
                clicker.clickforever()
            elif len(cmdlist) != 1:
                if len(cmdlist) == 2:
                    if "/t" in cmdlist:
                        try:
                            _times_ = int(input("请输入连点次数："))
                        except:
                            print("输入有误")
                        else:
                            clicker.clicktime(_times_)
                    elif "/v" in cmdlist:
                        try:
                            v = float(input("请输入点击间隔时长（浮点数，单位：秒）："))
                        except:
                            print("输入有误")
                        else:
                            print("连点开始")
                            clicker.clickv(v)
                if len(cmdlist) > 3:
                    print("参数过多")
                if len(cmdlist) == 3:
                    if cmdlist[1] != "/t" or cmdlist[1] != "/v" or cmdlist[2] != "/t" or cmdlist[2] != "/v":
                        if cmdlist[1] != "/t" or cmdlist[1] != "/v":
                            print("未知开关 - "+cmdlist[1].strip("/"))
                        else:
                            print("未知开关 - "+cmdlist[2].strip("/"))
                    else:
                        try:
                            _times_ = int(input("请输入连点次数："))
                        except:
                            print("输入有误")
                        else:
                            try:
                                v = float(input("请输入点击间隔时长（浮点数，单位：秒）："))
                            except:
                                print("输入有误")
                            else:
                                clicker.clicktimev(_times,v)
        elif "imgviewer" == cmdlist[0] or "IMGVIEWER" == cmdlist[0]:
            imgviewer.main()
        elif "stmt" == cmdlist[0] or "STMT" == cmdlist[0]:
            statement = open("声明.txt")
            print("\n"+statement.read())
        elif "fp" == cmdlist[0] or "FP" == cmdlist[0]:
            fp.main()
        elif "find" == cmdlist[0] or "FIND" == cmdlist[0]:
            if len(cmdlist) == 3:
                string = cmdlist[1]
                path = cmdlist[2]
                if thepath == "rep":
                    path = aduser + path
                else:
                    pass

                listOfLines  =  list()
                listin = list()
                with open (path,"r") as myfile:
                    for line in myfile:
                        listOfLines.append(line.strip())
                for i in range(len(listOfLines)):
                    if string in listOfLines[i]:
                        listin.append(i)
                print("\n---------- "+path)
                if not listin:
                    pass
                else:
                    print(listOfLines[i])
                
                myfile.close()
            else:
                print("命令语法不正确")
        else:
            if "help" == cmdlist[0] or "HELP" == cmdlist[0]:
                if len(cmdlist) > 2:
                    print("HELP [command]")
                    print("    command - 显示该命令的帮助信息")
                    print("HELP命令参数过多，请检查")
                if len(cmdlist) == 1:
                    print("目前ECD只收录了5个命令")
                    print("HELP [command]可显示命令的详细内容")
                    print("cls:清除屏幕")
                    print("time:显示当前时间")
                    print("ver:显示电脑版本")
                    print("exit:退出")
                    print("tree:以图形显示路径的文件夹结构")
                    print("type:显示文本文件的内容")
                    print("rename(ren):更改文件名称")
                    print("mkdir(md):创建文件夹")
                    print("rmdir(rm):删除空文件夹")
                    print("rmdirall(ECD专有命令):删除文件夹（文件夹可以不空）")
                    print("calc:打开windows计算器")
                    print("update:显示版本更新")
                    print("start:打开cmd")
                    print("absp:路径改为绝对路径")
                    print("rep:路径改为相对路径")
                    print("cd(chdir):显示或更改当前目录")
                    print("edit:快捷设置")
                    print("clicker(ECD专有命令):启用连点器")
                    print("imgviewer(ECD专有命令):启用图片查看器")
                    print("stmt:显示声明")
                    print("fp:打开File Processer")
                    print("find:在文件中寻找字符串（目前不够完善）")
                if len(cmdlist) == 2:
                    if cmdlist[1] == "cls" or cmdlist[1] == "CLS":
                        print("清除屏幕")
                        print("使用方法：")
                        print("cls")
                    if cmdlist[1] == "time" or cmdlist[1] == "TIME":
                        print("显示当前时间")
                        print("使用方法：")
                        print("time")
                    if cmdlist[1] == "ver" or cmdlist[1] == "VER":
                        print("显示电脑版本")
                        print("使用方法：")
                        print("ver")
                    if cmdlist[1] == "exit" or cmdlist[1] == "EXIT":
                        print("退出ECD")
                        print("使用方法：")
                        print("exit")
                    if cmdlist[1] == "tree" or cmdlist[1] == "TREE":
                        print("以图形的形式显示出路径的文件夹结构")
                        print("使用方法：")
                        print("tree [path]")
                        print("path - 路径")
                    if cmdlist[1] == "type" or cmdlist[1] == "TYPE":
                        print("显示文本文件的内容")
                        print("使用方法：")
                        print("type [path]filename")
                        print("path - 路径")
                        print("filename - 文件名")
                    if cmdlist[1] in ["rename","ren","RENAME","REN"]:
                        print("更改文件名称")
                        print("使用方法：")
                        print("rename [path]filename1 filename2")
                        print("ren [path]filename1 filename2")
                        print("path - filename1的文件路径")
                        print("filename1 - 需要重命名的文件")
                        print("filename2 - 重命名名称（需带上文件后缀名，否则文件类型会变为“文件”）")
                    if cmdlist[1] in ["mkdir","md","MKDIR","MD"]:
                        print("创建文件夹")
                        print("使用方法：")
                        print("mkdir [drive:]path")
                        print("md [drive:]path")
                        print("drive - 驱动器")
                        print("path - 文件夹路径（名称）")
                        print("特殊用法：")
                        print("mkdir drive:\\a\\b\\c")
                        print("若文件夹a不存在，那么将会在drive:下创建a文件夹，a下创建b文件夹，b下创建c文件夹")
                    if cmdlist[1] in ["rmdir","rd","RMDIR","RD"]:
                        print("删除空文件夹")
                        print("使用方法：")
                        print("rmdir /s /q [drive:]path")
                        print("rd /s /q [drive:]path")
                        print("/s - 删除父目录和所有子目录、文件（也可使用ECD专有命令rmdirall）")
                        print("/q - 安静模式。在命令中有/s的情况下会弹出确认问题，加上/q可去除问题")
                        print("若文件路径中包含空格，需在路径头和尾加上双引号")
                    if cmdlist[1] in ["rmdirall","RMDIRALL"]:
                        print("ECD专有命令，删除文件夹")
                        print("使用方法：")
                        print("rmdirall [drive:]path")
                        print("此命令可删除非空文件夹，也可使用rmdir /s")
                        print("若文件路径中包含空格，需在路径头和尾加上双引号")
                    if cmdlist[1] == "calc" or cmdlist[1] == "CALC":
                        print("打开计算器")
                        print("使用方法：")
                        print("calc")
                    if cmdlist[1] == "update" or cmdlist[1] == "UPDATE":
                        print("显示版本更新")
                        print("使用方法：")
                        print("update")
                    if cmdlist[1] == "start" or cmdlist[1] == "START":
                        print("打开cmd")
                        print("使用方法：")
                        print("start")
                        print("此命令也可打开文件或网址")
                        print("方法：")
                        print("start [url]")
                        print("url - 网址（需为‘www.’开头）")
                        print("start [path]")
                        print("path - 路径")
                    if cmdlist[1] == "absp" or cmdlist[1] == "ABSP":
                        print("将路径改为绝对路径")
                        print("使用方法：")
                        print("absp")
                        print("提示：设置后所有路径必须为绝对路径")
                    if cmdlist[1] == "rep" or cmdlist[1] == "REP":
                        print("将路径改为相对路径")
                        print("使用方法：")
                        print("rep")
                        print("提示：设置后所有路径必须为相对路径")
                    if cmdlist[1] in ["cd","CD","chdir","CHDIR"]:
                        print("显示或更改当前目录")
                        print("使用方法：")
                        print("cd path")
                        print("chdir path")
                        print("path - 路径")
                    if cmdlist[1] == "edit" or cmdlist[1] == "EDIT":
                        print("快捷设置")
                        print("使用方法：")
                        print("edit")
                    if cmdlist[1] == "clicker" or cmdlist[1] == "CLICKER":
                        print("启用连点器")
                        print("使用方法：")
                        print("clicker [/t] [/v]")
                        print("t - 指定点击次数")
                        print("v - 指定点击速度")
                        print("暂时无法同时使用")
                    if cmdlist[1] == "imgviewer" or cmdlist[1] == "IMGVIEWER":
                        print("启用图片查看器")
                        print("使用方法")
                        print("imgviewer")
                    if cmdlist[1] == "stmt" or cmdlist[1] == "STMT":
                        print("显示声明")
                        print("使用方法：")
                        print("stmt")
                    if cmdlist[1] == "fp" or cmdlist[1] == "FP":
                        print("打开File Processer（文件处理器）")
                        print("使用方法：")
                        print("fp")
                    if cmdlist[1] == "help" or cmdlist[1] == "HELP":
                        print("提供ECD命令的帮助信息")
                        print("使用方法：")
                        print("HELP [command]")
                        print("    command - 显示该命令的详细内容")
                    if cmdlist[1] == "find" or cmdlist[1] == "FIND":
                        print("在文件中寻找字符串")
                        print("使用方法：")111
                        print("find string path")
                        print("string - 要寻找的字符串")
                        print("path - 寻找的文件路径")
                    if cmdlist[1] not in ALLCMD:
                        print("'"+cmdlist[1]+"'"+"命令未收录")
            else:
                print("'"+cmdlist[0]+"'"+"命令未收录")
    except IndexError:
        pass
