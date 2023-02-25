import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.filedialog as fd
import sys
import webbrowser
import os
import pyperclip
import shutil
def intro():
    msgbox.showinfo("ECD.FP介绍","ECD（Easy CMD）是作者陈昕宇制作的Python模拟命令行程序，大部分命令用Python代码实现，没有过于依赖os.system，此工具FP（File Processer）是ECD第一个旗下重要实用工具（连点器、图片查看器虽在其之前，但并非重要工具），用于对文件进行处理（删除、重命名、显示等）")
def openecd():
    webbrowser.open("https://code.xueersi.com/home/project/detail?lang=code&pid=40496011&version=offline&form=python&langType=python")
def openfile():
    path = fd.askopenfilename()
    try:
        os.startfile(path)
    except:
        pass
def filepath():
    path = fd.askopenfilename()
    if not path:
        pass
    else:
        paste = msgbox.askyesno("获取成功","获取成功，路径名为："+path+" ，是否复制？")
        if paste == True:
            pyperclip.copy(path)
            msgbox.showinfo("复制成功","复制成功")
        else:
            pass
def rmfl(path):
    can = msgbox.askokcancel("警告","警告，即将删除文件，为防止误操作，请点击确定删除文件。")
    if can == True:
        os.remove(path=path)
        try:
            fpag.destroy()
        except:
            pass
    else:
        pass
def fpall():
    path = fd.askopenfilename()
    if not path:
        pass
    else:
        def openpath(path):
            pathgui = tk.Tk()
            pathgui.geometry("800x50")
            pet = tk.Entry(pathgui)
            pet.grid(ipadx=800,ipady=25)
            
            pet.insert(tk.END,path)
            pathgui.mainloop()
        def cpf(path):
            try:
                filename = fd.asksaveasfilename(initialfile=str(a.split("/")[-1]))
                shutil.copyfile(path,filename)
                msgbox.showinfo("复制成功","复制成功，路径："+filename)
            except:
                msgbox.showinfo("出现问题","文件选择时出现问题，请再次尝试。")
        fpag = tk.Tk()
        fpag.title("文件处理")
        if len(path) > 50 and len(path) < 70:
            fpag.geometry("600x400")
            viewpath = False
        elif len(path) > 70:
            fpag.geometry("500x400")
            newpath = path[0:15] + "...文件路径过长，点击文件路径可显示全部"
            viewpath = True
        else:
            fpag.geometry("500x400")
            viewpath = False
        if viewpath == True:
            fpfnl = tk.Label(fpag,text="路径:"+newpath,fg="black",font=("optima",10),cursor="hand2")
            fpfnl.bind("<Button-1>",lambda event:openpath(path))
        else:
            fpfnl = tk.Label(fpag,text="路径:"+path,fg="black",font=("optima",10))
        fpfnl.grid(row=0,column=0)
        cpbt = tk.Button(fpag,text="复制路径",font=("楷体",10),cursor="hand2",command=lambda:(pyperclip.copy(path),msgbox.showinfo("复制成功","复制成功")))
        cpbt.grid(row=0,column=1,padx=20)
        rnet = tk.Entry(fpag)
        rnet.grid(row=1,column=0,sticky="w")
        rnet.insert(tk.END,str(path.split("/")[-1]))
        rnbt = tk.Button(fpag,text="重命名文件",font=("楷体",10),cursor="hand2",command=lambda:(os.rename(path,path.strip(path.split("/")[-1])+rnet.get()),msgbox.showinfo("重命名成功","重命名成功")))
        rnbt.grid(row=1,column=1)
        cpfbt = tk.Button(fpag,text="复制到",font=("楷体",10),cursor="hand2",command=lambda:cpf(path))
        cpfbt.grid(row=2,column=0,sticky="w",ipadx=10,ipady=10)
        #rmbt = tk.Button(fpag,text="删除文件",bg="red",fg="yellow",font=("楷体",10),cursor="hand2",command=lambda:rmfl(path))
        #rmbt.grid(row=2,column=0,sticky="w")
        fpag.mainloop()
def main():
    main = tk.Tk()
    main.geometry("500x400")
    main.title("ECD FileProcesser v1.0.0")
    head = tk.Menu(main)
    tools = tk.Menu(head)
    file = tk.Menu(tools,tearoff=False)
    file.add_command(label="打开文件",command=openfile)
    file.add_command(label="获取文件路径",command=filepath)
    tools.add_cascade(label="文件",menu=file)
    about = tk.Menu(head,tearoff=False)
    about.add_command(label="关于",command=intro)
    about.add_command(label="打开ECD",command=openecd)
    head.add_cascade(label="介绍",menu=about)
    head.add_cascade(label="工具",menu=tools)
    fpa = tk.Button(main,text="单文件全方位处理",font=("楷体",15),cursor="hand2",command=fpall)
    fpa.grid(row=0,column=0,ipady=10,ipadx=10)
    main.config(menu=head)
    main.mainloop()