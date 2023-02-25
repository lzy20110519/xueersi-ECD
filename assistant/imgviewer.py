#图片查看器 陈昕宇制作 借鉴网络
#版本号：v1.0.0.202302021044
#已上线
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog       #获取文件全路径

def main():
    root=tk.Tk()  
    root.title('图片查看器 陈昕宇制作v1.0.0.202302021044')     
    root.geometry('500x500')     
    
    canvas=tk.Canvas(root,height=400)   #画布长款定为400x400
    canvas.pack()
    
    def openpicture():
        global img
        filename=filedialog.askopenfilename()     #获取文件全路径
        image=Image.open(filename)        #打开图片放到image中
        w,h=image.size     #获取image的长和宽
        mlength=max(w,h)    #取最大的一边作为缩放的基准
        mul=400/mlength    #缩放倍数
        w1=int(w*mul)
        h1=int(h*mul)
        re_image=image.resize((w1,h1))
        img=ImageTk.PhotoImage(re_image)    #在canvas中展示图片
        canvas.create_image(200,200,anchor='center',image=img)   #以中小点为锚点
     
    b=tk.Button(root,text='选择图片', command=openpicture)  #设置按钮，并给它openpicture命令
    b.pack()
    
    root.mainloop()
