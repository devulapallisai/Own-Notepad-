from tkinter import *
from tkinter.ttk import *
import os
from tkinter.font import *
from tkinter import simpledialog
import time
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showerror, showinfo

def OpenGoogle():
    try:
        from pywhatkit import search
        sea = simpledialog.askstring(
            title="Search", prompt="What do you want to search")
        if(str(sea) != "None" and str(sea) != "none" and str(sea) != ""):
            search(sea)
    except Exception as e:
        showerror("No Internet", "Oops Something went wrong we cannot connect to internet. Please check your internet connection and try again later")
def changefont(Desired):
    try:
        fonts=simpledialog.askstring("font","Which font you want?")
        Desired['family']=fonts
    except Exception as e:
        showinfo("Sorry","The font you want is currently unavaialable please try again later")
def Newe(event):
    global file
    root.title('Untitled -Notepad++')
    file = None
    TextArea.delete(1.0, END)
def New():
    global file
    root.title('Untitled -Notepad++')
    file = None
    TextArea.delete(1.0, END)
def About():
    showinfo("About notepad", "Created by Sai Prachodhan Devulapalli and serves purpose of writing something useful in it when we require we open it and see it.")
def clear():
    TextArea.delete("1.0", "end-1c")
def Cut():
    TextArea.event_generate(("<<Cut>>"))
def Copy():
    TextArea.event_generate(("<<Copy>>"))
def Paste():
    TextArea.event_generate(("<<Paste>>"))
def Darkmode():
    TextArea['bg']='Black'
    TextArea['fg']='White'
def Help():
    showinfo("Some Basic instructions", " --> Please note that notepad is for your writing purpose and you click on the notepad and write anyting you want.\n\n --> For saving file Click on the File and click on submenu option Save or Save As as you want in the directory you want.")
    showinfo("Some Basic instructions", " --> For Turning into Dark mode please click on Format and then choose Dark mode.\n\n --> You can also see there is option to change font and select that for changing font and fontsize and all.")
def Helpe():
    showinfo("Some Basic instructions", " --> Please note that notepad is for your writing purpose and you click on the notepad and write anyting you want.\n\n --> For saving file Click on the File and click on submenu option Save or Save As as you want in the directory you want.")
    showinfo("Some Basic instructions", " --> For Turning into Dark mode please click on Format and then choose Dark mode.\n\n --> You can also see there is option to change font and select that for changing font and fontsize and all.")
def DateandTime():
    time_label = Label(text=str(time.asctime(
        time.localtime(time.time()))), pady=4, font="Arial 19 bold")
    time_label.pack()
def Opene(event):
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if(file == ""):
        file = None
    else:
        root.title(os.path.basename(file)+" -Notepad++")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def Open():
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if(file == ""):
        file = None
    else:
        root.title(os.path.basename(file)+" -Notepad++")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
def saveFilee(event):
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

root = Tk()
root.geometry("850x450")
root.minsize(400, 400)
Desired=Font(family="lucida",size="13")

# For title and favicon at the top of tkinter window

root.wm_iconbitmap('notepad.ico')
root.title("Untitled -Notepad++")
Mainmenu = Menu(root)

# This is file menu and its submenus

Filesubmenu = Menu(Mainmenu, tearoff=0)
Filesubmenu.add_command(label="New      Ctrl+n", command=New)
Filesubmenu.add_command(label="Open     Ctrl+o", command=Open)
Filesubmenu.add_separator()
Filesubmenu.add_command(label="Save As   Ctrl+s", command=saveFile)
Filesubmenu.add_separator()
Filesubmenu.add_command(label="Exit       Ctrl+q", command=quit)
Mainmenu.add_cascade(label="File", menu=Filesubmenu)

# This is for Edit menu and its sub menus

Editmenu = Menu(Mainmenu, tearoff=0)
Editmenu.add_command(label="Cut", command=Cut)
Editmenu.add_command(label="Copy", command=Copy)
Editmenu.add_command(label="Paste", command=Paste)
Editmenu.add_separator()
Editmenu.add_command(label="Replace")
Editmenu.add_command(label="Clear All", command=clear)
Editmenu.add_command(label="Date and time", command=DateandTime)
Mainmenu.add_cascade(label="Edit", menu=Editmenu)

# This is for Format menu and its submenus

Fontmenu = Menu(Mainmenu, tearoff=0)
font = "lucida"
fontsize = "13"
Fontmenu.add_command(label="Change Font",command=lambda: changefont(Desired))
Fontmenu.add_command(label="Turn to dark mode", command=Darkmode)
Mainmenu.add_cascade(label="Format", menu=Fontmenu)

# for adding Help option

Helpmenu = Menu(Mainmenu, tearoff=0)
Helpmenu.add_command(label="About", command=About)
Helpmenu.add_command(label="Ask Google", command=OpenGoogle)
Helpmenu.add_command(label="Help", command=Help)
Mainmenu.add_cascade(label="Help", menu=Helpmenu)
root.config(menu=Mainmenu)

# Add Text area here and fill with default Font style lucida

TextArea = Text(root,bg="White",fg="Black")
file = None
TextArea.pack(expand=True, fill=BOTH)
TextArea.configure(font=Desired)

# Add a scroll bar for Text Area

scroll = Scrollbar(TextArea,cursor="hand1")
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)

# For taking events on the notepad

root.bind('<Control-q>', quit)
root.bind('<Control-s>', saveFilee)
root.bind('<Control-n>', Newe)
root.bind('<Control-o>', Opene)
root.bind('<Control-h>', Helpe)
root.mainloop()
