import tkinter
from tkinter import messagebox
from db import db
from mainPage import mainPage
class LoginPage:
    def __init__(self,master):
        self.root = master
        self.root.geometry("300x180")       # 窗口大小 宽 * 高
        self.username = tkinter.StringVar()
        self.password = tkinter.StringVar()

        self.page = tkinter.Frame(root)
        self.page.pack()
        tkinter.Label(self.page).grid(row=0, column=0)

        tkinter.Label(self.page, text='账户: ').grid(row=1, column=1)
        tkinter.Entry(self.page, textvariable=self.username).grid(row=1, column=2)

        tkinter.Label(self.page, text='密码: ').grid(row=2, column=1, pady=10)
        tkinter.Entry(self.page, textvariable=self.password).grid(row=2, column=2)

        tkinter.Button(self.page, text='登录', command=self.login).grid(row=3, column=1, pady=10)
        tkinter.Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=2)

    def login(self):
        name = self.username.get()
        pwd = self.password.get()
        flag, msg = db.checkLogin(name, pwd)
        if flag:
            self.page.destroy()
            mainPage(self.root)
        else:
            messagebox.showwarning(title='警告', message=msg)


if __name__ == '__main__':
    root = tkinter.Tk()
    LoginPage(master=root)
    root.mainloop()