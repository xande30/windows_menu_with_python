from tkinter import *  # get widget classes
from tkinter.messagebox import *  # get standard dialogs


class NewMenuDemo(Frame):  # an extended frame
    def __init__(self, parent=None):  # attach to top-level?

        Frame.__init__(self, parent)  # do superclass init
        self.pack(expand=YES, fill=BOTH)
        self.createWidgets()  # attach frames/widgets
        self.master.title("Toolbars and Menus")  # set window-manager info
        self.master.iconname("tkpython")  # label when iconified

    def createWidgets(self):
        self.makeMenuBar()
        self.makeToolBar()
        L = Label(self, text='Windows Menu And Toolbar View', font='Helvetica 18 bold')
        L.config(relief=SUNKEN, width=40, height=10, fg='red', bg='black')
        L.pack(expand=YES, fill=BOTH)

    def makeToolBar(self):
        toolbar = Frame(self, cursor='hand2', relief=SUNKEN, bd=2)
        toolbar.pack(side=BOTTOM, fill=X)
        Button(toolbar, text='Quit',background='black', fg='red', command=self.quit).pack(side=RIGHT)
        Button(toolbar, text='Hello',background='black', fg='red', command=self.greeting).pack(side=LEFT)

    def makeMenuBar(self):
        self.menubar = Menu(self.master, background='black', fg='red')
        self.master.config(menu=self.menubar)  # master=top-level window
        self.fileMenu()
        self.editMenu()
        self.imageMenu()

    def fileMenu(self):
        pulldown = Menu(self.menubar,background='black', fg='red')
        pulldown.add_command(label='Open...', command=self.notdone)
        pulldown.add_command(label='Quit', command=self.quit)
        self.menubar.add_cascade(label='File', underline=0, menu=pulldown)

    def editMenu(self):
        pulldown = Menu(self.menubar,background='black', fg='red')
        pulldown.add_command(label='Paste', command=self.notdone)
        pulldown.add_command(label='Spam', command=self.greeting)
        pulldown.add_separator()
        pulldown.add_command(label='Delete', command=self.greeting)
        pulldown.entryconfig(4, state=DISABLED)
        self.menubar.add_cascade(label='Edit', underline=0, menu=pulldown)

    def imageMenu(self):
        photoFiles = ('hellopython.gif', 'mr.gif', 'nice.gif')
        pulldown = Menu(self.menubar)
        self.photoObjs = []
        for file in photoFiles:
            img = PhotoImage(file='..//pythonProject//' + file)
        pulldown.add_command(image=img, command=self.notdone)
        self.photoObjs.append(img)  # keep a reference
        self.menubar.add_cascade(label='Image', underline=0, menu=pulldown)

    def greeting(self):
        showinfo('greeting', 'Greetings')

    def notdone(self):
        showerror('Not implemented', 'Not yet available')

    def quit(self):
        if askyesno('Verify quit', 'Are you sure you want to quit?'):
            Frame.quit(self)


if __name__ == '__main__': NewMenuDemo().mainloop()  # if I'm run as a script
