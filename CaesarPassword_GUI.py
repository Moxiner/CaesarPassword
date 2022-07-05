# 导入模块
from tkinter import END, messagebox
import tkinter as tk
import ttkbootstrap as ttk
import time

# 初始变量
VERSION = "1.1 GUI版"
AUTHOR = "Moxiner"
Themo = "DARK"

# 加密
def LockPassword() :
    password = Input.get()
    Key = []
    for p in password:
        if "a" <= p <= "z" :
             Key.append(chr(ord("a") + (ord(p) - ord("a") + 3)%26))
        elif "A" <= p <= "Z" :
             Key.append(chr(ord("A") + (ord(p) - ord("A") + 3)%26))
        else:
             Key.append(p)
    Key = ''.join(Key)
    Key = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime()) + " [加密成功] 密码为 " + Key
    Output.insert("end" ,f"{Key}\n")
    Input.delete(0,END)
    print(Key)



# 解密
def KeyPassword() :
    password = Input.get()
    Key = []
    for p in password:
        if "a" <= p <= "z" :
            Key.append(chr(ord("a") + (ord(p) - ord("a") - 3)%26))
        elif "A" <= p <= "Z" :
            Key.append(chr(ord("A") + (ord(p) - ord("A") - 3)%26))
        else:
            Key.append(p)
    Key = ''.join(Key)
    Key = time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime()) + " [解密成功] 密码为 " + Key
    Output.insert("end", f"{Key}\n")
    Input.delete(0,END)
    print(Key)


# GUI
Window = tk.Tk()
Window.title("CawsarPassword")
Window.geometry("500x340+300+300")
Label = tk.Label(Window ,text="请输入内容").place(x=250 ,y=10 ,anchor="n")
Label = tk.Label(Window ,text=f"v{VERSION} Author:{AUTHOR} ").place(x=490 ,y=335 ,anchor="se")
Input = ttk.Entry(Window ,width=70 , bootstyle=Themo)
Input.place(x=250 ,y=40 ,anchor="n")
LockButton = ttk.Button(Window ,text="加密" ,width=15, command=LockPassword , bootstyle=Themo).place(x=260, y=80 ,anchor="nw")
KeyButton = ttk.Button(Window ,text="解密" , width=15, command=KeyPassword , bootstyle=Themo).place(x=240 ,y=80 , anchor="ne")
Output = ttk.Text(Window , height=10 ,width=70 )
Output.place(x=250 ,y=120 ,anchor="n")

# 主程序
Window.mainloop()