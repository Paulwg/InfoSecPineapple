#! /usr/bin/env python
from tkinter.constants import *
from tkinter import *

class App(Frame):
    '''
    GUI interface
    '''
    @classmethod
    def main(cls):
        GUI = Tk()
        app = cls(GUI)
        app.grid(sticky=NSEW)
        GUI.title('Pineapplegedon')
        GUI.rowconfigure(app, pad=6)
        GUI.columnconfigure(app, pad=6)
        GUI.resizable(True, True)
        GUI.mainloop()

    def __init__(self, GUI):
        super().__init__(GUI)
        self.create_variables()
        self.create_widgets()
        self.grid_widgets()

    def create_variables(self):
        self.MODES = [
            ("AppCompatCache"),
            ("Process Table"),
            ("Prefetch"),
            ("Network Connections"),
            ("Auto Runs"),
            ("Sched Tasks"),
            ("Startup Folders"),
            ("Services"),
            ("Installed Software"),
            ("Unsigned Executables"),
            ("Installed Drivers"),
            ("ADS"),
            ("Dir Walk"),
            ("VSC Walk,Timestamps"),
            ("MFT timestamps"),
        ]
        self.a = StringVar()
        self.a.set("A")
        self.c = IntVar()
        self.i = 6
        self.d = 0

    def create_widgets(self):
        menu = Menu(self.master)

        filemenu = Menu(self, tearoff=0)
        filemenu.add_command(label="New", command=None)
        filemenu.add_command(label="Open...",command= None)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=None)
        menu.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(self, tearoff=0)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=None)

        self.label1 = Label(self, text="Computer Name:")
        self.label2 = Label(self, text="IP Address:")
        self.label3 = Label(self, text="Username:")
        self.label4 = Label(self, text="Password:")
        self.label5 = Label(self, text="Path:")

        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry4 = Entry(self)
        self.entry5 = Entry(self)

        self.button1 = Radiobutton(self,text="Local",variable=self.c,value=0,indicatoron=0)#local or remote
        self.button2 = Radiobutton(self,text="Remote",variable=self.c,value=1,indicatoron=0)

        self.buttonlist = Radiobutton(self)#List of Selections

        self.submit = Button(self, text="Submit", command=self.execute)

        self.master.config(menu=menu)

    def grid_widgets(self):
        options1 = dict(sticky=NSEW)
        #top bar
        
        self.label1.grid(row = 0,**options1)
        self.label2.grid(row = 1,**options1)
        self.label3.grid(row = 2,**options1)
        self.label4.grid(row = 3,**options1)
        self.label5.grid(row = 4,**options1)
        self.button1.grid(row = 5,column = 0,**options1)
        self.button2.grid(row = 5,column = 1,**options1)

        self.entry1.grid(row = 0,column = 1)
        self.entry2.grid(row = 1,column = 1)
        self.entry3.grid(row = 2,column = 1)
        self.entry4.grid(row = 3,column = 1)
        self.entry5.grid(row = 4,column = 1)

        for text in self.MODES:
            self.buttonlist = Radiobutton(self,text=text,variable=self.a,value=text,
                            anchor=W,justify=LEFT,width=16,command=self.select)
            self.buttonlist.grid(row = self.i,column=self.d)
            if(self.d == 1):
                self.i += 1
                self.d = 0
                continue
            if(self.d == 0):
                self.d = 1
                continue
        
        self.submit.grid(row = self.i+1,columnspan=2,pady=4,sticky=NSEW)

        
    #To be completed functions

    def select(self):
        self.radioButt = str(self.a.get())
        self.ComputerName = self.entry1.get()
        self.Ipaddress = self.entry2.get()
        self.User = self.entry3.get()
        self.Passw = self.entry4.get()
        self.TarPath = self.entry5.get()

    def Make_Decision_Local_Remote(self,arg):
        import Juice
        MethodToBeCalled = arg
        if(self.c.get() == 0):
            Juice.Juice(0,MethodToBeCalled)
        if(self.c.get() == 1):
            Juice.Juice(1,MethodToBeCalled)
    
    def execute(self):
        arg = self.radioButt.replace(" ","_")        
        self.Make_Decision_Local_Remote(arg)
    

if __name__ == '__main__':
    App.main()
