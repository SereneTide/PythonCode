import tkinter
from views import AboutFrame, ChangeFrame, DeleteFrame, InsertFrame, SearchFrame


class mainPage:
    def __init__(self, master):
        self.root = master
        self.root.geometry('600x400')  # 窗口大小 宽 * 高
        self.createPage()
    def createPage(self):
        self.aboutFrame = AboutFrame(self.root)
        self.changeFrame = ChangeFrame(self.root)
        self.deleteFrame = DeleteFrame(self.root)
        self.insertFrame = InsertFrame(self.root)
        self.searchFrame = SearchFrame(self.root)
        menubar = tkinter.Menu(self.root)
        menubar.add_command(label='录入', command=self.showInsert)
        menubar.add_command(label='查询', command=self.showSearch)
        menubar.add_command(label='删除', command=self.showDelete)
        menubar.add_command(label='修改', command=self.showChange)
        menubar.add_command(label='关于', command=self.showAbout)
        self.root['menu'] = menubar
    def showChange(self):
        self.aboutFrame.pack_forget()
        self.deleteFrame.pack_forget()
        self.insertFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.changeFrame.pack()

    def showInsert(self):
        self.aboutFrame.pack_forget()
        self.deleteFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.insertFrame.pack()
    def showDelete(self):
        self.aboutFrame.pack_forget()
        self.insertFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.deleteFrame.pack()
    def showSearch(self):
        self.aboutFrame.pack_forget()
        self.deleteFrame.pack_forget()
        self.insertFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.searchFrame.pack()
    def showAbout(self):
        self.deleteFrame.pack_forget()
        self.insertFrame.pack_forget()
        self.searchFrame.pack_forget()
        self.changeFrame.pack_forget()
        self.aboutFrame.pack()
if __name__ == '__main__':
    root = tkinter.Tk()
    mainPage(root)
    root.mainloop()
