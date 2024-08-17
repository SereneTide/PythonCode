import tkinter
from tkinter import ttk
from db import db

class AboutFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        tkinter.Label(self, text="关于").pack()

class ChangeFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tkinter.StringVar()
        self.parent1 = tkinter.StringVar()
        self.parent2 = tkinter.StringVar()
        self.parent3 = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.createPage()
    def createPage(self):
        tkinter.Label(self).grid(row=0, pady=10)

        tkinter.Label(self, text='姓 名:').grid(row=0, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.name).grid(row=0, column=2, pady=10)

        tkinter.Label(self, text='parent1 :').grid(row=1, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.parent1).grid(row=1, column=2, pady=10)

        tkinter.Label(self, text='parent2 :').grid(row=2, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.parent2).grid(row=2, column=2, pady=10)

        tkinter.Label(self, text='parent3 :').grid(row=3, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.parent3).grid(row=3, column=2, pady=10)

        tkinter.Button(self, text='查询', command=self.searchInfo).grid(row=4, column=1, pady=10)
        tkinter.Button(self, text='修改', command=self.changeInfo).grid(row=4, column=2, pady=10)
        tkinter.Label(self, textvariable=self.status).grid(row=5, column=1, pady=10)
    def searchInfo(self):
        flag, info = db.search(self.name.get())
        if flag:
            self.name.set(info['username'])
            self.parent1.set(info['parent1'])
            self.parent2.set(info['parent2'])
            self.parent3.set(info['parent3'])
            self.status.set('查询成功')
        else:
            self.status.set(info)
    def changeInfo(self):
        pass
class InsertFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.name = tkinter.StringVar()
        self.parent1 = tkinter.StringVar()
        self.parent2 = tkinter.StringVar()
        self.parent3 = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.createPage()
    def createPage(self):
        tkinter.Label(self).grid(row=0, pady=10)

        tkinter.Label(self, text='姓 名:').grid(row=0, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.name).grid(row=0, column=2, pady=10)

        tkinter.Label(self, text='parent1 :').grid(row=1, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.parent1).grid(row=1, column=2, pady=10)

        tkinter.Label(self, text='parent2 :').grid(row=2, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.parent2).grid(row=2, column=2, pady=10)

        tkinter.Label(self, text='parent3 :').grid(row=3, column=1, pady=10)
        tkinter.Entry(self, textvariable=self.parent3).grid(row=3, column=2, pady=10)

        tkinter.Button(self, text='录入', command=self.recodeInfo).grid(row=4, column=3, pady=10)

        tkinter.Label(self, textvariable=self.status).grid(row=4, column=1, pady=10)

    def recodeInfo(self):
        student = {"username": self.name.get(), "parent1": self.parent1.get(), "parent2": self.parent2.get(), "parent3": self.parent3.get() }
        self.name.set('')
        self.parent1.set('')
        self.parent2.set('')
        self.parent3.set('')
        db.insert(student)
        self.status.set('获取数据成功')
class DeleteFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.username = tkinter.StringVar()
        self.status = tkinter.StringVar()
        tkinter.Label(self, text='根据名字删除').pack()
        tkinter.Entry(self, textvariable=self.username).pack()
        tkinter.Button(self, text='删除', command=self.delete).pack(pady=10, anchor=tkinter.E)
        tkinter.Label(self, textvariable=self.status).pack()
    def delete(self):
        username = self.username.get()
        flag, msg = db.delete(username)
        self.status.set(msg)

class SearchFrame(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.tableView = tkinter.Frame()
        self.tableView.pack()
        self.createPage()

    def createPage(self):
        columns = ('username', 'parent1', 'parent2', 'parent3')
        # columnsValue = ('姓名', 'parent1', 'parent2', 'parent3')
        self.treeView = ttk.Treeview(self, show='headings', columns=columns)
        self.treeView.column('username', anchor='center', width=80)
        self.treeView.column('parent1', anchor='center', width=80)
        self.treeView.column('parent2', anchor='center', width=80)
        self.treeView.column('parent3', anchor='center', width=80)
        self.treeView.heading('username', text='姓名')
        self.treeView.heading('parent1', text='parent1')
        self.treeView.heading('parent2', text='parent2')
        self.treeView.heading('parent3', text='parent3')
        self.treeView.pack(fill=tkinter.BOTH, expand=True)
        self.showDataFrame()

        tkinter.Button(self, text='刷新', command=self.showDataFrame).pack(anchor=tkinter.E, pady=5)
    def showDataFrame(self):
        for _ in map(self.treeView.delete, self.treeView.get_children('')):
            pass
        students = db.all()
        index = 0
        for student in students:
            self.treeView.insert('', index + 1,
                values=(student['username'], student['parent1'], student['parent2'], student['parent3']))


