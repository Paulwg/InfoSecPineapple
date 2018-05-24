#! /usr/bin/env python
from tkinter.constants import *
from tkinter import *
from tkinter import ttk
import sys
import Local
import Remote

class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''
    def __init__(self,text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self,str):
        self.text_area.insert("end",str)
        
class App(Frame):
    '''
    GUI interface
    '''
    @classmethod
    def main(cls):
        GUI = Tk()
        app = cls(GUI)
        app.config(bg='black', border='15')
        app.grid(sticky=NSEW)
        GUI.title('Pineapplegedon')
        GUI.resizable(True, True)
        GUI.iconbitmap(r'..\Images\Pineapplegedon.ico')
        GUI.frame = Frame()
        GUI.mainloop()

    def __init__(self, GUI):
        super().__init__(GUI)
        self.create_variables()
        self.create_widgets()
        self.grid_widgets()
        r = self.redirector()
        
    def redirector(self, inputStr=""):
        '''
        Redirect StdOut to entry box. Called once in main()    
        '''
        sys.stdout = StdoutRedirector(self.entry6)
        self.entry6.insert(END, inputStr)

    def CLRoutput(self):
        self.entry6.config(state=NORMAL)
        self.entry6.delete(1.0,END)

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
        self.a = StringVar()#Setting Vars for the two radiobutton groups
        self.a.set("A")
        self.c = IntVar()
        self.i = 6# row. Counter for the grid of artifact collection radiobutton options
        self.d = 0#column

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

        self.master.config(menu=menu)#binding instance as menu

        self.label1 = Label(self, text="Computer Name:",font='system 10',bg='cyan')
        self.label2 = Label(self, text="IP Address:",font='system 10',bg='cyan')
        self.label3 = Label(self, text="Username:",font='system 10',bg='cyan')
        self.label4 = Label(self, text="Password:",font='system 10',bg='cyan')
        self.label5 = Label(self, text="Path:",font='system 10',bg='cyan')

        self.entry1 = Entry(self,font='system 10',bg='alice blue')
        self.entry2 = Entry(self,font='system 10',bg='alice blue')
        self.entry3 = Entry(self,font='system 10',bg='alice blue')
        self.entry4 = Entry(self,font='system 10',bg='alice blue')
        self.entry5 = Entry(self,font='system 10',bg='alice blue')

        self.button1 = Radiobutton(self,text="Local",variable=self.c,value=0,indicatoron=0,font='system 10',bg='cyan',selectcolor='purple')#local 0 or remote 1
        self.button2 = Radiobutton(self,text="Remote",variable=self.c,value=1,indicatoron=0,font='system 10',bg='cyan',selectcolor='purple')

        self.buttonlist = Radiobutton(self,font='system 9',bg='spring green')#List of Selections

        self.submit = Button(self, text="Submit", command=self.execute,font='system 10',bg='cyan')

        self.entry6 = Text(self,height=25,width=100,bg='alice blue')
        self.clearoutput = Button(self, text="Clear Output", command=self.CLRoutput,font='system 9',bg='cyan')
        self.scrollbar = Scrollbar(self)

        self.entry6.config(yscrollcommand= self.scrollbar.set)#Pairing scrollbar with text entry
        self.scrollbar.config(command=self.entry6.yview,troughcolor='yellow')

    def grid_widgets(self):
        options1 = dict(sticky=NSEW)
        
        self.label1.grid(row = 0,padx=2,pady=1,**options1)#ComputerName
        self.label2.grid(row = 1,padx=2,pady=1,**options1)#IP Address
        self.label3.grid(row = 2,padx=2,pady=1,**options1)#Username
        self.label4.grid(row = 3,padx=2,pady=1,**options1)#Password
        self.label5.grid(row = 4,padx=2,pady=1,**options1)#Path
        
        self.button1.grid(row = 5,column = 0,padx=2,pady=2,**options1)#Local
        self.button2.grid(row = 5,column = 1,padx=2,pady=2,**options1)#Remote

        self.entry1.grid(row = 0,column = 1)#Entry for ComputerName
        self.entry2.grid(row = 1,column = 1)#Entry for IP Address
        self.entry3.grid(row = 2,column = 1)#Entry for Username
        self.entry4.grid(row = 3,column = 1)#Entry for Password
        self.entry5.grid(row = 4,column = 1)#Entry for Path

        for text in self.MODES:#Grid for list of radiobuttons
            self.buttonlist = Radiobutton(self,text=text,variable=self.a,value=text,pady=2,
                            anchor=W,font='system 9',bg='cyan',activebackground='purple',justify=LEFT,width=16,command=self.select)#command calls to select when new button is clicked
            self.buttonlist.grid(row = self.i,column=self.d)
            if(self.d == 1):
                self.i += 1
                self.d = 0
                continue
            if(self.d == 0):
                self.d = 1
                continue
        
        self.submit.grid(row = self.i+1,columnspan=2,pady=4,sticky=NSEW)#Submit button

        self.clearoutput.grid(row=0,column=4,padx=2,pady=1,)#results clear
        self.entry6.grid(row=1,column=4,rowspan=12,padx=3)#Results entry box
        self.scrollbar.grid(row=1,column=5,rowspan=12,sticky=N+S+W)#scrollbar
        

    def select(self):#called from radiobutton selection
        '''
        Getters for the user selections.
        '''
        self.radioButt = str(self.a.get())
        self.ComputerName = self.entry1.get()
        self.Ipaddress = self.entry2.get()
        self.User = self.entry3.get()
        self.Passw = self.entry4.get()
        self.TarPath = self.entry5.get()
    
    def execute(self):#called from pressing submit button
        arg = self.radioButt.replace(" ","_")#replace space in name with underscore        
        self.Make_Decision_Local_Remote(arg)

    def Make_Decision_Local_Remote(self,arg):#called from execute
        MethodToBeCalled = arg
        if(self.c.get() == 0):
            Juice(0,MethodToBeCalled)
        if(self.c.get() == 1):
            Juice(1,MethodToBeCalled)

class Juice(object):
    '''
    Calls either Local or Remote class queries by selected methodname.
    '''    
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.main()
        
    def main(self):
        methodname = self.arg2
        if(self.arg1 == 0):# 0 represents local query
            print("Querying Local Machine for: ", methodname)
            result = getattr(Local.Local, methodname)#method to be called that is an attribut of the class
            result()#print result for redirect of stdout            
        if(self.arg1 == 1 ):
            result = getattr(Remote.Remote, methodname)
            result()
    

if __name__ == '__main__':
    App.main()
