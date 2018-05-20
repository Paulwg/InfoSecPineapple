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
            ("AppCompatCache", "1"),
            ("Process Table","2"),
            ("Prefetch","3"),
            ("Network Connections","4"),
            ("Auto Runs","5"),
            ("Sched Tasks","6"),
            ("Startup Folders","7"),
            ("Services","8"),
            ("Installed Software","9"),
            ("Unsigned Executables","10"),
            ("Installed Drivers","11"),
            ("ADS","12"),
            ("Dir Walk","13"),
            ("VSC Walk,Timestamps","14"),
            ("MFT timestamps","15"),
        ]
        self.v = StringVar()
        self.v.set("L")
        self.i = 4
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

        self.entry1 = Entry(self)
        self.entry2 = Entry(self)
        self.entry3 = Entry(self)
        self.entry4 = Entry(self)

        self.b = Radiobutton(self)

        self.submit = Button(self, text="Submit", command=self.execute)

        self.master.config(menu=menu)

    def grid_widgets(self):
        options1 = dict(sticky=NSEW)
        #top bar
        
        self.label1.grid(row = 0,**options1)
        self.label2.grid(row = 1,**options1)
        self.label3.grid(row = 2,**options1)
        self.label4.grid(row = 3,**options1)

        self.entry1.grid(row = 0,column = 1)
        self.entry2.grid(row = 1,column = 1)
        self.entry3.grid(row = 2,column = 1)
        self.entry4.grid(row = 3,column = 1)

        for text, mode in self.MODES:
            self.b = Radiobutton(self,text=text,variable=self.v,value=mode,
                            anchor=W,justify=LEFT,width=16,command=self.sel)
            self.b.grid(row = self.i,column=self.d)
            if(self.d == 1):
                self.i += 1
                self.d = 0
                continue
            if(self.d == 0):
                self.d = 1
                continue
        
        self.submit.grid(row = self.i+1,columnspan=2,pady=4,sticky=NSEW)

        
    #To be completed functions

    def Login(self):
        pass

    def sel(self):
        self.radioButt = int(self.v.get())
        self.ComputerName = self.entry1.get()
        self.Ipaddress = self.entry2.get()
        self.User = self.entry3.get()
        self.Passw = self.entry4.get()

    def execute(self):
        print(self.radioButt)
        print(self.ComputerName, self.Ipaddress, self.User, self.Passw)


if __name__ == '__main__':
    App.main()